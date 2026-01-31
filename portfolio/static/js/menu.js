document.addEventListener("DOMContentLoaded", () => {
  const menuToggle = document.getElementById("menu-toggle");
  const navMenu = document.getElementById("nav-menu");
  const menuClose = document.getElementById("menu-close");

  if (!menuToggle || !navMenu || !menuClose) return;

  menuToggle.addEventListener("click", () => {
    navMenu.classList.add("active");
  });

  menuClose.addEventListener("click", () => {
    navMenu.classList.remove("active");
  });

  document.querySelectorAll(".nav-link").forEach(link => {
    link.addEventListener("click", () => {
      navMenu.classList.remove("active");
    });
  });
});
