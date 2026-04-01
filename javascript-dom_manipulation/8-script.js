document.addEventListener('DOMContentLoaded', function () {
  const helloTag = document.getElementById('hello');

  fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
    .then(response => response.json())
    .then(data => {
      helloTag.textContent = data.hello;
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
