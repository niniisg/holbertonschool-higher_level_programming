document.addEventListener('DOMContentLoaded', (event) => {
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(reponse => response.json())
    .then(data => {
    const div = document.getElementById('hello');
    div.textContent = data.hello

    })
    
    .catch(error => console.error('Error:', error));
    });