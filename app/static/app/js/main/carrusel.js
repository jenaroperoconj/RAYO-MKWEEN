let currentSlide = 0;

function showSlide(index) {
    const slides = document.querySelectorAll('.carousel-slide');
    if (index >= slides.length) currentSlide = 0;
    if (index < 0) currentSlide = slides.length - 1;
    document.querySelector('.carousel-container').style.transform = `translateX(${-currentSlide * 100}%)`;
}

function moveSlide(n) {
    showSlide(currentSlide += n);
}

document.addEventListener('DOMContentLoaded', () => {
    showSlide(currentSlide);
});
