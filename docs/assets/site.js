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
  const target = location.hash && document.getElementById(location.hash.slice(1));
  const group = target?.closest('details');
  if (group && !group.open) {
    group.open = true;
    group.scrollIntoView({ block: 'start' });
  }
};
window.addEventListener('hashchange', openTarget);
openTarget();
