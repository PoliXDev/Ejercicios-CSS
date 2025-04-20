import './style/main.scss'

// Función para manejar el scroll y agregar efectos
document.addEventListener('DOMContentLoaded', () => {
  // Animación de aparición para las secciones al hacer scroll
  const sections = document.querySelectorAll('section');
  
  const observerOptions = {
    root: null,
    rootMargin: '0px',
    threshold: 0.1
  };
  
  const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);
  
  sections.forEach(section => {
    section.classList.add('fade-in');
    observer.observe(section);
  });
  
  // Agregar comportamiento al botón de Sign Up
  const signUpBtn = document.querySelector('.btn-primary');
  if (signUpBtn) {
    signUpBtn.addEventListener('click', () => {
      alert('¡Gracias por tu interés! El formulario de registro se abrirá pronto.');
    });
  }
});
