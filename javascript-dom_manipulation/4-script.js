document.addEventListener('DOMContentLoaded', (event) => {
let addI = document.querySelector('#add_item');
let lis = document.querySelector('.my_list')
addI.addEventListener('click', () => {
    let newli = document.createElement('li');
    newli.textContent = "Item";
    lis.appendChild(newli);

});
});