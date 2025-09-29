const checkboxes = document.querySelectorAll('.tag-checkbox');
function updateSelected() {
  const selected = Array.from(checkboxes)
  .filter(cb => cb.checked)
  .map(cb => cb.value);
  console.log('Selecionados:', selected.join(', '));
}
checkboxes.forEach(cb => cb.addEventListener('change', updateSelected));
updateSelected();