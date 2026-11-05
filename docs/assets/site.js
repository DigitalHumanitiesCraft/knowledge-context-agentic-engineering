// Progressive enhancement for the landing pages; all content works without it.
//
// Term definitions open on hover and keyboard focus through CSS alone. This
// script adds Escape to dismiss an open definition (WCAG 1.4.13) and lets a
// term that is a button, such as AI Harnesses, keep its definition open on
// click or tap.
const terms = document.querySelectorAll('.term');

const close = (term) => {
  term.classList.remove('term--open');
  term.querySelector('button.term-trigger')?.setAttribute('aria-expanded', 'false');
};

for (const term of terms) {
  const button = term.querySelector('button.term-trigger');
  if (button) {
    button.setAttribute('aria-expanded', 'false');
    button.addEventListener('click', () => {
      const open = term.classList.toggle('term--open');
      term.classList.remove('term--dismissed');
      button.setAttribute('aria-expanded', String(open));
    });
  }
  term.addEventListener('mouseleave', () => term.classList.remove('term--dismissed'));
  term.addEventListener('focusout', (event) => {
    if (term.contains(event.relatedTarget)) return;
    term.classList.remove('term--dismissed');
    close(term);
  });
}

document.addEventListener('keydown', (event) => {
  if (event.key !== 'Escape') return;
  for (const term of terms) {
    if (term.matches(':hover, :focus-within, .term--open')) {
      term.classList.add('term--dismissed');
      close(term);
    }
  }
});

// On touch screens a pinned definition is a sheet at the bottom of the screen;
// a tap anywhere outside its term closes it.
document.addEventListener('pointerdown', (event) => {
  for (const term of terms) {
    if (term.classList.contains('term--open') && !term.contains(event.target)) close(term);
  }
});

// A link to a module, `#module-0N` or `#video-module-0N`, opens that module's
// group on arrival, so the reader lands on its videos instead of a closed row.
const openTarget = () => {
  const target = location.hash ? document.getElementById(location.hash.slice(1)) : null;
  const group = target?.closest('details');
  if (group && !group.open) {
    group.open = true;
    group.scrollIntoView({ block: 'start' });
  }
};
window.addEventListener('hashchange', openTarget);
openTarget();

// Glossary: search over the precomputed normalised field, a module filter and
// a switch between module and alphabetical order. Without this script the
// form stays hidden and every entry is listed by module with the jump list.
const tools = document.querySelector('.glossary-tools');
if (tools) {
  const fold = { ä: 'ae', ö: 'oe', ü: 'ue', ß: 'ss' };
  const normalise = (text) => text.toLowerCase().replace(/[äöüß]/g, (c) => fold[c])
    .normalize('NFD').replace(/[̀-ͯ]/g, '');
  const root = tools.closest('.glossary');
  const main = root.querySelector('.glossary-main');
  const entries = [...root.querySelectorAll('.glossary-entry')];
  const groups = [...root.querySelectorAll('.glossary-group')];
  const count = tools.querySelector('.glossary-tools__count');
  const letterLinks = [...tools.querySelectorAll('.glossary-letters a')];
  const lang = document.documentElement.lang || 'en';

  // Each module list remembers its entries, so the module order can be restored
  // after the alphabetical order has moved them.
  const homes = [...root.querySelectorAll('.glossary-group .glossary-list')]
    .map((list) => [list, [...list.children]]);

  // The alphabetical order is built once, a section per initial letter.
  const alpha = document.createElement('div');
  alpha.className = 'glossary-alpha';
  alpha.hidden = true;
  const letters = new Map();
  const sorted = [...entries].sort((a, b) => a.querySelector('dfn').textContent
    .localeCompare(b.querySelector('dfn').textContent, lang, { sensitivity: 'base' }));
  for (const entry of sorted) {
    const letter = entry.dataset.letter;
    if (!letters.has(letter)) {
      const section = document.createElement('section');
      section.className = 'glossary-group glossary-letter';
      section.id = `letter-${letter}`;
      section.setAttribute('aria-labelledby', `letter-${letter}-title`);
      section.innerHTML = `<h2 class="glossary-group__title" id="letter-${letter}-title">${letter}</h2><dl class="glossary-list"></dl>`;
      letters.set(letter, section);
      alpha.append(section);
    }
  }
  main.append(alpha);

  const setOrder = (order) => {
    const byLetter = order === 'letter';
    if (byLetter === !alpha.hidden) return;
    if (byLetter) {
      for (const entry of sorted) {
        letters.get(entry.dataset.letter).querySelector('dl').append(entry);
      }
    } else {
      for (const [list, children] of homes) list.append(...children);
    }
    alpha.hidden = !byLetter;
    for (const group of groups) group.classList.toggle('glossary-group--parked', byLetter);
    root.classList.toggle('glossary--letters', byLetter);
  };

  const state = () => ({
    q: tools.q.value.trim(),
    module: tools.module.value,
    order: tools.order.value,
  });

  // The address carries search, module and order, so a filtered view can be
  // shared and survives a reload; the fragment stays untouched.
  const remember = () => {
    const { q, module, order } = state();
    const params = new URLSearchParams();
    if (q) params.set('q', q);
    if (module) params.set('module', module);
    if (order !== 'module') params.set('order', order);
    const query = params.toString();
    history.replaceState(null, '', `${location.pathname}${query ? `?${query}` : ''}${location.hash}`);
  };

  const apply = (announce = true) => {
    const { q, module, order } = state();
    setOrder(order);
    const words = normalise(q).split(/\s+/).filter(Boolean);
    let shown = 0;
    for (const entry of entries) {
      const visible = (!module || entry.dataset.module === module)
        && words.every((word) => entry.dataset.search.includes(word));
      entry.hidden = !visible;
      if (visible) shown += 1;
    }
    for (const section of [...groups, ...letters.values()]) {
      section.hidden = section.classList.contains('glossary-group--parked')
        || !section.querySelector('.glossary-entry:not([hidden])');
    }
    // Counted from the entries, because in module order the letter sections are empty.
    const live = new Set(entries.filter((entry) => !entry.hidden).map((entry) => entry.dataset.letter));
    for (const link of letterLinks) link.toggleAttribute('aria-disabled', !live.has(link.dataset.letter));
    if (!announce) return;
    const { template, one, none } = count.dataset;
    count.textContent = shown === 0 ? none : shown === 1 ? one : template.replace('{n}', shown);
  };

  // A link to an entry or letter the current view hides clears the filter
  // and keeps the order the reader chose.
  const reveal = () => {
    const target = location.hash ? document.getElementById(location.hash.slice(1)) : null;
    if (!target?.closest('[hidden]')) return;
    const order = tools.order.value;
    tools.reset();
    tools.order.value = order;
    if (target.id.startsWith('letter-')) tools.order.value = 'letter';
    apply();
    remember();
    target.scrollIntoView({ block: 'start' });
  };

  // A letter belongs to the alphabetical order, so choosing one switches to it
  // before the browser follows the link.
  for (const link of letterLinks) {
    link.addEventListener('click', (event) => {
      if (link.hasAttribute('aria-disabled')) {
        event.preventDefault();
        return;
      }
      if (tools.order.value !== 'letter') {
        tools.order.value = 'letter';
        apply();
        remember();
      }
    });
  }

  document.addEventListener('keydown', (event) => {
    const typing = event.target.closest?.('input, textarea, select, [contenteditable]');
    const shortcut = ((event.ctrlKey || event.metaKey) && event.key.toLowerCase() === 'k')
      || (event.key === '/' && !typing);
    if (shortcut) {
      event.preventDefault();
      tools.q.focus();
      tools.q.select();
    }
  });

  const params = new URLSearchParams(location.search);
  if (params.has('q')) tools.q.value = params.get('q');
  if (params.has('module')) tools.module.value = params.get('module');
  if (params.get('order') === 'letter') tools.order.value = 'letter';

  tools.hidden = false;
  root.classList.add('glossary--enhanced');
  tools.addEventListener('input', () => {
    apply();
    remember();
  });
  tools.addEventListener('submit', (event) => event.preventDefault());
  window.addEventListener('hashchange', reveal);
  // The browser may restore a search or filter on back navigation.
  apply(Boolean(tools.q.value || tools.module.value));
  reveal();
}

// The language control keeps the fragment, so a linked term stays in view
// when the reader switches between the paired pages.
const keepFragment = () => {
  for (const link of document.querySelectorAll('.language-nav a[href]')) {
    link.hash = location.hash;
  }
};
window.addEventListener('hashchange', keepFragment);
keepFragment();
