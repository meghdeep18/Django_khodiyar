document.addEventListener('DOMContentLoaded', () => {
    // Container animation on load
    gsap.from('.container', {
        duration: 1.5,
        opacity: 0,
        y: -50,
        ease: 'elastic.out(1, 0.8)'
    });

    // Input fields animation with a slight delay and stagger effect
    gsap.from('.input-group', {
        duration: 0.8,
        opacity: 0,
        y: 20,
        stagger: 0.2,
        ease: 'power3.out',
        delay: 0.5
    });

    // Button appearance animation
    gsap.from('button', {
        duration: 0.8,
        opacity: 0,
        y: 20,
        ease: 'power3.out',
        delay: 1.5
    });

    // Submit animation and container effect on form submit
    const form = document.getElementById('signupForm');
    form.addEventListener('submit', (e) => {
        e.preventDefault();  // Prevent form submission until validation is complete

        // Get form values
        const username = document.getElementById('username').value.trim();
        const email = document.getElementById('email').value.trim();
        const password = document.getElementById('password').value.trim();
        const confirmPassword = document.getElementById('confirm-password') ? document.getElementById('confirm-password').value.trim() : password;

        // Validate the form fields
        const isValid = validateForm(username, email, password, confirmPassword);

        if (isValid) {
            // Proceed with form submission if validation is successful
            gsap.to('.container', {
                duration: 0.5,
                scale: 0.95,
                opacity: 0.8,
                backgroundColor: '#005662',
                ease: 'power3.inOut',
                onComplete: () => {
                    // Success message animation
                    gsap.to('.container', {
                        duration: 0.3,
                        scale: 0.9,
                        backgroundColor: '#00796b',
                        ease: 'elastic.out(1, 0.8)',
                        onComplete: () => {
                            alert('Sign up successful!');
                            form.reset();

                            // Reset animation to bring back the container
                            gsap.to('.container', {
                                duration: 0.5,
                                scale: 1,
                                opacity: 1,
                                backgroundColor: 'rgba(30, 30, 30, 0.8)',
                                ease: 'power3.out'
                            });
                        }
                    });
                }
            });
        }
    });

    // Form validation function
    function validateForm(username, email, password, confirmPassword) {
        // Regular expression for email format
        const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

        // Check if fields are empty
        if (!username || !email || !password || !confirmPassword) {
            showError('All fields must be filled.');
            return false;
        }

        // Username length check
        if (username.length < 3) {
            showError('Username must be at least 3 characters long.');
            return false;
        }

        // Email validation
        if (!emailPattern.test(email)) {
            showError('Please enter a valid email address.');
            return false;
        }

        // Password match check
        if (password !== confirmPassword) {
            showError('Passwords do not match.');
            return false;
        }

        return true;  // Validation passed
    }

    // Function to display error messages
    function showError(message) {
        const errorBox = document.querySelector('.error-message');
        if (!errorBox) {
            const newErrorBox = document.createElement('div');
            newErrorBox.className = 'error-message';
            newErrorBox.style.color = 'red';
            newErrorBox.style.marginTop = '10px';
            newErrorBox.textContent = message;
            form.appendChild(newErrorBox);
        } else {
            errorBox.textContent = message;
        }

        // Animate error message appearance
        gsap.fromTo('.error-message', { opacity: 0, y: -10 }, { opacity: 1, y: 0, duration: 0.5, ease: 'power3.out' });
    }
});
