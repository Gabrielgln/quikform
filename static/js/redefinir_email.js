function emailValidation() {
    var emailInput = document.querySelector('input[name="email"]');
    var value = emailInput.value;
    if (!/^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/.test(value)) {
        emailInput.setCustomValidity('Insira um email válido');
    } else {
        emailInput.setCustomValidity('');
    }
}