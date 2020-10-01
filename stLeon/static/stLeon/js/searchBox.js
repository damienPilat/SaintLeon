// Create a Search Box element


// Get All searchbox instances
var searchBox = document.getElementsByClassName("search-box");

// Create Input element w/ attributes
var search_input = document.createElement("input");
Object.assign(search_input, {
    className: 'search-txt',
    type: 'text',
    placeholder: 'Rechercher'
});

// Create link tag w/ attributes
var search_link = document.createElement("a");
Object.assign(search_link, {
    className: 'search-btn center-all',
    href: '#'
});
// Create & Append image to link tag
var search_img = document.createElement("img");
Object.assign(search_img, {
    src: SEARCH_ICON_STATIC_URL,
    id: 'search-icon'
});
search_link.appendChild(search_img);


// Append elements to search boxes
for(i=0; i<searchBox.length;i++) {
    searchBox[i].appendChild(search_input);
    searchBox[i].appendChild(search_link);
}