document.addEventListener("DOMContentLoaded", () => {
  const toggleButton = document.getElementById('theme-toggle');
  const html = document.documentElement;

  // Restaurar tema salvo
  const savedTheme = localStorage.getItem('theme');
  if (savedTheme) html.setAttribute('data-theme', savedTheme);

  // Só adiciona evento se o botão existir
  if (toggleButton) {
    toggleButton.addEventListener('click', (e) => {
      e.preventDefault(); // evita que # apareça na URL
      const current = html.getAttribute('data-theme');
      const next = current === 'light' ? 'dark' : 'light';
      html.setAttribute('data-theme', next);
      localStorage.setItem('theme', next);
      updateIcon(toggleButton, html);
    });

    updateIcon(toggleButton, html);
  }
});

function updateIcon(button, html) {
  const icon = button.querySelector('i');
  const current = html.getAttribute('data-theme');
  if (current === 'light') {
    icon.classList.remove('fa-moon');
    icon.classList.add('fa-sun');
  } else {
    icon.classList.remove('fa-sun');
    icon.classList.add('fa-moon');
  }
}
