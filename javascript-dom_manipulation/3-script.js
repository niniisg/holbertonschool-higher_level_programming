document.addEventListener('DOMContentLoaded', (event) => {
    let toge = document.querySelector('#toggle_header');
    let header = document.querySelector('header');
    
    toge.addEventListener('click', () => {
        if (header.classList.contains('red')) {
            header.classList.remove('red');
            header.classList.add('green');
        } else if (header.classList.contains('green')){
            header.classList.remove('green');
            header.classList.add('red');

        }
    
    });
    });