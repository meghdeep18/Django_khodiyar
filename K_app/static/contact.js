document.addEventListener('DOMContentLoaded', () => {
    // GSAP animation for the container
    gsap.from('.container', {
        opacity: 0,
        y: 50,
        duration: 1,
        ease: 'power3.out'
    });

    // GSAP animations for left section elements
    gsap.from('.left-section > *', {
        opacity: 0,
        x: -50,
        stagger: 0.2,
        duration: 0.8,
        ease: 'power3.out',
        delay: 0.5
    });

    // GSAP animations for form elements
    gsap.from('.form-group', {
        opacity: 0,
        y: 20,
        stagger: 0.2,
        duration: 0.8,
        ease: 'power3.out',
        delay: 0.5
    });

    gsap.from('.submit-btn', {
        opacity: 0,
        y: 20,
        duration: 0.8,
        ease: 'power3.out',
        delay: 1.3
    });

    // Optional: Floating label effect for form inputs
    const inputs = document.querySelectorAll('input, textarea');
    inputs.forEach(input => {
        input.addEventListener('focus', () => {
            input.parentNode.classList.add('focused');
        });
        input.addEventListener('blur', () => {
            if (input.value === '') {
                input.parentNode.classList.remove('focused');
            }
        });
    });

    // Scroll to Top Button functionality
    const scrollToTopBtn = document.getElementById('scrollToTopBtn');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 200) {
            scrollToTopBtn.style.display = 'flex';
        } else {
            scrollToTopBtn.style.display = 'none';
        }
    });

    scrollToTopBtn.addEventListener('click', () => {
        gsap.to(window, { scrollTo: { y: 0 }, duration: 1, ease: 'power2.inOut' });
    });
});
