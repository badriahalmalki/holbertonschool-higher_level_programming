document.addEventListener('DOMContentLoaded', function () {
  const characterTag = document.getElementById('character');

  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
      characterTag.textContent = data.name;
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
