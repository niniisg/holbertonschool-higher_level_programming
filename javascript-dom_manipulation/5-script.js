document.addEventListener('DOMContentLoaded', (event) => {
    let update = document.querySelector('#update_header');
    let header = document.querySelector('header');
    update.addEventListener('click', () => {
        header.textContent = "New Header!!!";
    });
});