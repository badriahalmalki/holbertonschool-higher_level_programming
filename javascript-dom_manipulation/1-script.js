document.addEventListener('DOMContentLoaded', function () {
  const redHeader = document.getElementById('red_header');
  const header = document.querySelector('header');

  redHeader.addEventListener('click', function () {
    header.style.color = '#FF0000';
  });
});
