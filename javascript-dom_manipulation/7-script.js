document.addEventListener('DOMContentLoaded', (event) => {
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
.then(reponse => response.json())
.then(data => {
    const ul = document.getElemetebyId('list-movies')
    data.results.forEach(movie => {

     const li = document.createElement('li');
     li.textContent = movie.title;
      ul.appendChild(li)


});
})

.catch(error => console.error('Error:', error));
});