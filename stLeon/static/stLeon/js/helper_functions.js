
// OPEN LINKS IN NEW TABS
// -> Implemented for links in visite slides
var links = document.getElementsByClassName("visite-txt-link");

for (var i = 0; i<links.length; i++) {
    links[i].setAttribute('target', '_blank');
}