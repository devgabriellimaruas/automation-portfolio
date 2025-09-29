document.addEventListener('DOMContentLoaded', () => {
    const buttons = document.querySelectorAll('.filter-btn');
    
    buttons.forEach(button => {
      button.addEventListener('click', () => {
        const type = button.dataset.type;
        const url = new URL(window.location.href);
        
        const current = url.searchParams.get('type');
        
        if (current === type) {
          url.searchParams.delete('type');
        } else {
          url.searchParams.set('type', type);
        }
        
        window.location.href = url.toString();
      });
    });
  });