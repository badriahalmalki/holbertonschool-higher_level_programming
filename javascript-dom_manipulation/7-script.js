document.addEventListener('DOMContentLoaded', function () {
  const list = document.getElementById('list_movies');

  fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
      data.results.forEach(movie => {
        const li = document.createElement('li');
        li.textContent = movie.title;
        list.appendChild(li);
      });
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
