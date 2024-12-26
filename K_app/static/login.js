document.getElementById('loginForm').addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent form submission

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Simulated login validation
    if (username === "admin" && password === "password") {
        alert("Login successful!");
        // Redirect or perform desired actions
    } else {
        alert("Invalid username or password. Please try again.");
    }
});
