const checkboxes = document.querySelectorAll('.tag-checkbox');
  const selectedDisplay = document.getElementById('selected-tools');

  function updateSelected() {
    const selected = Array.from(checkboxes)
      .filter(cb => cb.checked)
      .map(cb => cb.value);
    selectedDisplay.textContent = selected.length ? 'Selecionados: ' + selected.join(', ') : 'Selecionados: Nenhum';
  }

  checkboxes.forEach(cb => cb.addEventListener('change', updateSelected));
  updateSelected();