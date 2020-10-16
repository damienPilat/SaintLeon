
// OPEN LINKS IN NEW TABS
// -> Implemented for links in visite slides
// Get elements
var links = document.getElementsByClassName("visite-txt-link");

// Set _blank attribute
for (var i = 0; i<links.length; i++) {
    links[i].setAttribute('target', '_blank');
}

// CUSTOM COLORS FOR INFO LINES
// -> Implemented for border in main-info elements
// Array of colours
const borderColors = ['rgb(20,20,20', 'rgb(200,50,12', 'rgb(50,250,200'];

// Get Elements
const info_elements = document.getElementsByClassName('info-slot');
// Set borderLeft
for (var j = 0; j < info_elements.length; j++) {
    info_elements[j].style.borderLeft = '3px solid '+borderColors[j];
}