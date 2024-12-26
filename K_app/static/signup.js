document.getElementById('loginForm').addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent form submission
    const email = document.getElementById('email').values;
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Simulated login validation
    if (username === "admin" && password === "password") {
        alert("signup successful!");
        // Redirect or perform desired actions
    } else {
        alert("Invalid email or password. Please try again.");
    }
});
