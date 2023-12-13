function checkCredentials() {
    // Test credentials
    const testUsers = ['admin', 'david', 'brandon', 'steven'];
    const testPassword = '123';

    // Get user input
    const usernameInput = document.getElementById('username').value;
    const passwordInput = document.getElementById('password').value;

    // Check if the entered username is one of the test users and the password matches
    if (testUsers.includes(usernameInput) && passwordInput === testPassword) {
        document.getElementById("loginStatus").textContent = '';
        document.getElementById('username').value = '';
        document.getElementById('password').value = '';
        window.location.href = 'https://netflix.zeabur.app/contact/list';
    } else {
        document.getElementById("loginStatus").textContent =
            "Usuario o contraseña incorrectos. Por favor, intenta de nuevo.";
    }
}