'use strict';

// This is an intentionally deterministic UI sketch, not a deployed AI agent.
// Keeping the distinction visible prevents a portfolio illustration from being
// mistaken for a validated personalized-learning model.
const branches = Object.freeze({
  wrong: Object.freeze({
    tag: 'NEXT / REBUILD THE MODEL',
    title: 'Use the same pizza.',
    description: 'If identical pizzas are shared among 6 or 8 people, which person gets the bigger slice? Explain without comparing the denominator digits.',
    reason: 'REASON: DENOMINATOR MISCONCEPTION',
  }),
  guess: Object.freeze({
    tag: 'NEXT / TEST THE REASONING',
    title: 'Explain why 1/6 wins.',
    description: 'You selected the larger fraction. Can you justify it using equal-size diagrams, or give a new example with 1/4 and 1/5?',
    reason: 'REASON: UNCERTAIN UNDERSTANDING',
  }),
});

function activatePath(path) {
  const next = branches[path];
  if (!next) return;
  const title = document.getElementById('next-title');
  const description = document.getElementById('next-description');
  const tag = document.getElementById('next-tag');
  const reason = document.getElementById('next-reason');
  if (!title || !description || !tag || !reason) return;
  title.textContent = next.title;
  description.textContent = next.description;
  tag.textContent = next.tag;
  reason.textContent = next.reason;
  for (const button of document.querySelectorAll('[data-path]')) {
    button.setAttribute('aria-pressed', String(button.dataset.path === path));
  }
}

for (const button of document.querySelectorAll('[data-path]')) {
  button.addEventListener('click', () => activatePath(button.dataset.path));
}

// Keep the navigation indicator tied to the selected same-page destination.
const portfolioNavLinks = [...document.querySelectorAll('.site-nav a[href^="#"]')];
function markCurrentSection() {
  const selected = window.location.hash || '#work';
  for (const link of portfolioNavLinks) {
    const current = link.getAttribute('href') === selected;
    link.classList.toggle('is-active', current);
    if (current) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  }
}
window.addEventListener('hashchange', markCurrentSection);
markCurrentSection();
