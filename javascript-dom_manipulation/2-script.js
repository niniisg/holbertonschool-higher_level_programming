document.addEventListener('DOMContentLoaded', (event) => {
    let redh = document.querySelector('#red_header');
    let header = document.querySelector('header');
    
    redh.addEventListener('click', () => {
        header.classList.add('red');
    });
    });