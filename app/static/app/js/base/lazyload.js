document.addEventListener('DOMContentLoaded', function() {
    let lazyImages = document.querySelectorAll('.lazyload');
    lazyImages.forEach(img => {
        img.src = img.dataset.src;
    });
});