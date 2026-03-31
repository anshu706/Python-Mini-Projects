/* main.js – C Mini Projects Showcase */

/* ============================
   Category filter
   ============================ */
document.querySelectorAll('.pill').forEach(function (pill) {
  pill.addEventListener('click', function () {
    // Update active pill
    document.querySelectorAll('.pill').forEach(function (p) {
      p.classList.remove('active');
    });
    this.classList.add('active');

    var filter = this.dataset.filter;

    document.querySelectorAll('.card').forEach(function (card) {
      if (filter === 'all' || card.dataset.category === filter) {
        card.classList.remove('hidden');
      } else {
        card.classList.add('hidden');
      }
    });
  });
});

/* ============================
   Keyboard nav for cards
   ============================ */
document.querySelectorAll('.card').forEach(function (card) {
  card.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' || e.key === ' ') {
      e.preventDefault();
      card.click();
    }
  });
});

/* ============================
   Modal helpers
   ============================ */
var modalIds = {
  atm:       'modal-atm',
  billing:   'modal-billing',
  casino:    'modal-casino',
  guess:     'modal-guess',
  library:   'modal-library',
  periodic:  'modal-periodic',
  phonebook: 'modal-phonebook',
  quiz:      'modal-quiz',
};

function openModal(key) {
  var id = modalIds[key];
  if (!id) return;

  // Show overlay
  var overlay = document.getElementById('modalOverlay');
  overlay.classList.add('active');
  overlay.setAttribute('aria-hidden', 'false');

  // Show modal
  var modal = document.getElementById(id);
  modal.classList.add('active');

  // Focus the close button for accessibility
  var closeBtn = modal.querySelector('.modal-close');
  if (closeBtn) {
    setTimeout(function () { closeBtn.focus(); }, 50);
  }

  // Prevent body scroll
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  // Hide all modals
  document.querySelectorAll('.modal').forEach(function (m) {
    m.classList.remove('active');
  });

  // Hide overlay
  var overlay = document.getElementById('modalOverlay');
  overlay.classList.remove('active');
  overlay.setAttribute('aria-hidden', 'true');

  // Restore body scroll
  document.body.style.overflow = '';
}

// Close on Escape key
document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape') closeModal();
});

/* ============================
   Scroll-reveal animation
   ============================ */
var observer = new IntersectionObserver(
  function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'translateY(0)';
        observer.unobserve(entry.target);
      }
    });
  },
  { threshold: 0.1 }
);

document.querySelectorAll('.card').forEach(function (card, i) {
  card.style.opacity = '0';
  card.style.transform = 'translateY(20px)';
  card.style.transition = 'opacity 0.4s ease ' + i * 0.05 + 's, transform 0.4s ease ' + i * 0.05 + 's, border-color 0.2s ease, box-shadow 0.2s ease';
  observer.observe(card);
});
