document.addEventListener('DOMContentLoaded', () => {
    // GSAP animations on page load
    gsap.from('.login-box', { duration: 1, y: -50, opacity: 0, ease: 'power3.out' });

    const loginButton = document.getElementById('login-btn');

    // Button hover effect with GSAP
    loginButton.addEventListener('mouseover', () => {
        gsap.to(loginButton, { scale: 1.1, duration: 0.3, ease: 'power1.inOut' });
    });

    loginButton.addEventListener('mouseout', () => {
        gsap.to(loginButton, { scale: 1, duration: 0.3, ease: 'power1.inOut' });
    });

    // Button click animation
    loginButton.addEventListener('click', () => {
        gsap.to('.login-box', { y: -100, duration: 0.6, opacity: 0, ease: 'power3.inOut' });
        setTimeout(() => {
            alert("Login functionality to be implemented.");
            gsap.to('.login-box', { y: 0, duration: 0.6, opacity: 1, ease: 'power3.inOut' });
        }, 1000);
    });
});
