document.addEventListener('DOMContentLoaded', () => {
  const popups = document.querySelectorAll('#message-popup .popup');
  if (!popups.length) return;
  const lastPopup = popups[popups.length - 1];
  lastPopup.style.opacity = '0.95';
  lastPopup.style.transform = 'translateX(0)';
  setTimeout(() => {
    lastPopup.style.opacity = '0';
    lastPopup.style.transform = 'translateX(-20px)';
  }, 4000);
});
