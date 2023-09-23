window.addEventListener('resize', function () {
    var inputElement = document.getElementById('main');
    if (window.innerWidth <= 768) {
        inputElement.className = 'main uk-flex uk-flex-column uk-flex-middle uk-text-center';
    } else {
        inputElement.className = 'main uk-flex';
    }
});

window.addEventListener('resize', function () {
    var inputElement = document.getElementById('main2');
    if (window.innerWidth <= 768) {
        inputElement.className = 'main uk-flex uk-flex-column uk-flex-middle uk-text-center';
    } else {
        inputElement.className = 'main uk-flex';
    }
});

window.addEventListener('resize', function () {
    var inputElement = document.getElementById('name');
    if (window.innerWidth <= 768) {
        inputElement.className = 'uk-input uk-form-width-medium';
    } else {
        inputElement.className = 'uk-input uk-form-width-large';
    }
});
window.addEventListener('resize', function () {
    var inputElement = document.getElementById('email');
    if (window.innerWidth <= 768) {
        inputElement.className = 'uk-input uk-form-width-medium';
    } else {
        inputElement.className = 'uk-input uk-form-width-large';
    }
});
window.addEventListener('resize', function () {
    var inputElement = document.getElementById('pass');
    if (window.innerWidth <= 768) {
        inputElement.className = 'uk-input uk-form-width-medium';
    } else {
        inputElement.className = 'uk-input uk-form-width-large';
    }
});
window.addEventListener('resize', function () {
    var inputElement = document.getElementById('pass2');
    if (window.innerWidth <= 768) {
        inputElement.className = 'uk-input uk-form-width-medium';
    } else {
        inputElement.className = 'uk-input uk-form-width-large';
    }
});

window.addEventListener('resize', function () {
    var inputElement = document.getElementById('left');
    if (window.innerWidth <= 768) {
        inputElement.className = 'left uk-flex uk-flex-column uk-flex-center uk-text-center uk-width-expand';
    } else {
        inputElement.className = 'left uk-width-1-2 uk-flex uk-flex-column uk-flex-center uk-text-center';
    }
});

window.addEventListener('resize', function () {
    var inputElement = document.getElementById('right');
    if (window.innerWidth <= 768) {
        inputElement.className = 'right uk-flex uk-flex-column uk-flex-center uk-text-center uk-width-expand';
    } else {
        inputElement.className = 'right uk-width-1-2 uk-flex uk-flex-column uk-flex-center uk-text-center';
    }
});

window.addEventListener('resize', function () {
    var inputElement = document.getElementById('btn-submit');
    if (window.innerWidth <= 768) {
        inputElement.className = 'uk-button uk-button-primary uk-button-small';
    } else {
        inputElement.className = 'uk-button uk-button-primary uk-button-large uk-width-1-1';
    }
});