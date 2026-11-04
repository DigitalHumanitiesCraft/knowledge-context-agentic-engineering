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

// Video previews are hosted by YouTube, so they are requested only once a
// reader opens a module group. Without this script the cards show title and
// duration on a neutral plate and no request reaches YouTube.
for (const group of document.querySelectorAll('.video-module')) {
  group.addEventListener('toggle', () => {
    if (!group.open) return;
    for (const media of group.querySelectorAll('.video-card__media[data-thumb]')) {
      const img = document.createElement('img');
      img.className = 'video-card__thumbnail';
      img.src = media.dataset.thumb;
      img.alt = '';
      img.width = 320;
      img.height = 180;
      img.decoding = 'async';
      media.append(img);
      media.removeAttribute('data-thumb');
    }
  });
}

// A module link in the introduction targets its video group. Opening the group
// on arrival saves the second click; the toggle handler above then loads the
// previews, which follows the reader's own click on that link.
const openTarget = () => {
  const target = location.hash && document.getElementById(location.hash.slice(1));
  if (target instanceof HTMLDetailsElement && !target.open) {
    target.open = true;
    target.scrollIntoView({ block: 'start' });
  }
};
window.addEventListener('hashchange', openTarget);
openTarget();
// A repeated click on the same link fires no hashchange, so links open their
// group directly as well.
for (const link of document.querySelectorAll('a[href^="#video-module-"]')) {
  link.addEventListener('click', () => {
    const group = document.getElementById(link.hash.slice(1));
    if (group instanceof HTMLDetailsElement) group.open = true;
  });
}

// On touch screens a pinned definition is a sheet at the bottom of the screen;
// a tap anywhere outside its term closes it.
document.addEventListener('pointerdown', (event) => {
  for (const term of terms) {
    if (term.classList.contains('term--open') && !term.contains(event.target)) close(term);
  }
});
