// Adds event listeners to all the close-alert buttons
document.addEventListener('DOMContentLoaded', function () {
  const closeButtons = document.querySelectorAll('.close-alert');

  closeButtons.forEach(function(button) {
      button.addEventListener('click', function() {
          // Get the parent alert container and hide it
          const alert = button.closest('.flash');
          if (alert) {
              alert.style.display = 'none';  // Hides the element
          }
      });
  });
});