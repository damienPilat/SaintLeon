// SLIDESHOW for Visite Culturelle
var slideIndex = 1;
showSlides(slideIndex);

function currentSlide(n) {
    showSlides(slideIndex = n);
}

function showSlides(n) {
    var i;
    var slides = document.getElementsByClassName("slides-v");
    var navs = document.getElementsByClassName("visite-nav-link");

    // Remove active from all slide elements
    for (i = 0; i < slides.length; i++) {
        slides[i].className = slides[i].className.replace(" visite-active", "");
    }
    // Remove active from all nav elements
    for (i = 0; i < navs.length; i++) {
        navs[i].className = navs[i].className.replace(" visite-nav-active", "");
    }

    // Add active to correct element
    slides[slideIndex-1].className += " visite-active";

    // Add active to nav element
    navs[slideIndex-2].className += " visite-nav-active";
}