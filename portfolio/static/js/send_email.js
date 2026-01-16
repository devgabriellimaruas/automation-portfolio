const form = document.getElementById('contactForm');
const submitBtn = document.getElementById('submitBtn');

form.addEventListener('submit', function (event) {
    event.preventDefault();
    submitBtn.textContent = 'Enviando...';
    submitBtn.disabled = true;
    form.submit();
});
