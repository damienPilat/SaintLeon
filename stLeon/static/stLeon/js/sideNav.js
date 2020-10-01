// Functions to open and close Side Nav for reduced screen sizes

// Open Side Nav
function openNav() {
    document.getElementById('sideNav').style.width = "250px";
    document.getElementById("main").style.marginLeft = "250px";
    document.body.style.backgroundColor = "rgba(93,29,20,0.8)";
    detectClose(); // Allow usr to click on main screen area to close menu
}

// Close Side Nav
function closeNav() {
    document.getElementById('sideNav').style.width = "0";
    document.getElementById("main").style.marginLeft = "0";
    document.body.style.backgroundColor = "#EC4B33";
}

// Close sideNav w/ click on main
function detectClose() {
    // Wait 0.4s before activating listner
    setTimeout(function() {
        window.addEventListener('click', function(e) {
            if (document.getElementById('main').contains(e.target)) {
                closeNav();
            }
        }, 400); // 400milsecond delay (transition period)
    }) // END: setTimeout
} // END: detectClose