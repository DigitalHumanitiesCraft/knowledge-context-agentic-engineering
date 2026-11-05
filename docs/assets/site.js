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

// Glossary: search over the precomputed normalised field and a module filter.
// Without this script the form stays hidden and every entry is listed.
const tools = document.querySelector('.glossary-tools');
if (tools) {
  const fold = { ä: 'ae', ö: 'oe', ü: 'ue', ß: 'ss' };
  const normalise = (text) => text.toLowerCase().replace(/[äöüß]/g, (c) => fold[c])
    .normalize('NFD').replace(/[̀-ͯ]/g, '');
  const entries = [...document.querySelectorAll('.glossary-entry')];
  const groups = [...document.querySelectorAll('.glossary-group')];
  const count = tools.querySelector('.glossary-tools__count');
  const apply = (announce = true) => {
    const words = normalise(tools.q.value).split(/\s+/).filter(Boolean);
    const module = tools.module.value;
    let shown = 0;
    for (const entry of entries) {
      const visible = (!module || entry.dataset.module === module)
        && words.every((word) => entry.dataset.search.includes(word));
      entry.hidden = !visible;
      if (visible) shown += 1;
    }
    for (const group of groups) group.hidden = !group.querySelector('.glossary-entry:not([hidden])');
    if (!announce) return;
    const { template, one, none } = count.dataset;
    count.textContent = shown === 0 ? none : shown === 1 ? one : template.replace('{n}', shown);
  };
  // A jump link or term link to an entry the current filter hides clears the filter.
  const reveal = () => {
    const target = location.hash ? document.getElementById(location.hash.slice(1)) : null;
    if (!target?.closest('[hidden]')) return;
    tools.reset();
    apply();
    target.scrollIntoView({ block: 'start' });
  };
  tools.hidden = false;
  tools.addEventListener('input', () => apply());
  tools.addEventListener('submit', (event) => event.preventDefault());
  window.addEventListener('hashchange', reveal);
  // The browser may restore a search or filter on back navigation.
  apply(Boolean(tools.q.value || tools.module.value));
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
