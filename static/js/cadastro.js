function nameValidation() {
    let nomeInput = document.querySelector('input[name="nome"]');
    let value = nomeInput.value;
    if (/\d/.test(value)) {
        nomeInput.setCustomValidity('Não insira números');
    } else {
        nomeInput.setCustomValidity('');
    }
}

function emailValidation() {
    var emailInput = document.querySelector('input[name="email"]');
    var value = emailInput.value;
    if (!/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/.test(value)) {
        emailInput.setCustomValidity('Insira um email válido');
    } else {
        emailInput.setCustomValidity('');
    }
}

function passwordValidation() {
    let passwordInput = document.getElementById('password');
    let value = passwordInput.value;
    if (value.length < 8) {
        passwordInput.setCustomValidity('Insira pelo menos 8 caracteres');
    } else {
        passwordInput.setCustomValidity('');
    }
}

function passwordMatchValidation() {
    var passwordInput = document.getElementById('password');
    var confirmPasswordInput = document.querySelector('input[name="confirmPassword"]');
    if (passwordInput.value !== confirmPasswordInput.value) {
        confirmPasswordInput.setCustomValidity('As senhas não coincidem');
    } else {
        confirmPasswordInput.setCustomValidity('');
    }
}

document.querySelector('#form').addEventListener('submit', function(event) {
    if (!this.checkValidity()) {
        event.preventDefault();
    } else {
        showTermsError();
    }
});
