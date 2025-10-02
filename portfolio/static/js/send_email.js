const form = document.getElementById('contactsForm');
const submitBtn = document.getElementById('submitBtn');

form.addEventListener('submit', function (event) {
    event.preventDefault();
    submitBtn.textContent = 'Enviando...';
    submitBtn.disabled = true;
    form.submit();
});
