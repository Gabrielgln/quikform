document.addEventListener('DOMContentLoaded', function() {
    const menuItems = document.querySelectorAll('.menu-item');

    menuItems.forEach(function(item) {
        item.addEventListener('click', function() {
            const subMenu = this.querySelector('.sub-menu');
            subMenu.classList.toggle('active');
        });
    });
});
