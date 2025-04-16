// scripts.js

// Select elements to animate
const fadeIns = document.querySelectorAll('.fade-in');
const progressBars = document.querySelectorAll('.progress');

// Create an Intersection Observer
const observer = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      // Add fade-in animation
      entry.target.classList.add('visible');

      // Animate progress bars
      if (entry.target.classList.contains('progress')) {
        entry.target.style.width = entry.target.dataset.width;
      }
    }
  });
}, {
  threshold: 0.1
});

// Observe each fade-in and progress element
fadeIns.forEach(el => observer.observe(el));
progressBars.forEach(el => observer.observe(el));
