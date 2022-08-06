const menuBtn = document.querySelector('.menu-btn');
const section = document.querySelector('section');
const label = document.querySelector('label');
const closeBtn = document.querySelector('.close-btn');

menuBtn.addEventListener('click', function() {
    section.style.left = 0;
    menuBtn.style.opacity = 0;
})

closeBtn.addEventListener('blur', function() {
    section.style.left = '-200px';
})
