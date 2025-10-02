document.addEventListener('DOMContentLoaded', () => {

  const form = document.getElementById('project-form');
  const checkboxes = document.querySelectorAll('.tag-checkbox');

  // Função para obter os checkboxes selecionados
  function getSelectedTools() {
    return Array.from(checkboxes)
      .filter(cb => cb.checked)
      .map(cb => cb.value);
  }

  // Atualiza o console (opcional)
  function updateSelected() {
    const selected = getSelectedTools();
    console.log('Selecionados:', selected.join(', '));
  }

  checkboxes.forEach(cb => cb.addEventListener('change', updateSelected));
  updateSelected();

  // Validação antes de enviar o formulário
  form.addEventListener('submit', (e) => {
    const selected = getSelectedTools();

    if (selected.length === 0) {
      e.preventDefault(); // impede o envio
      alert('Selecione pelo menos uma ferramenta para o projeto!');
      return false;
    }

    // Opcional: mostrar mensagem de sucesso no envio (antes do redirect)
    // alert('Formulário enviado com sucesso!');
  });

});
