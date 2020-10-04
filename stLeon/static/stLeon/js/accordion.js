var acc = document.getElementsByClassName("accordion");
var otherPanels = document.getElementsByClassName("panel");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].addEventListener("click", function() {
        // Toggle active on current element
        this.classList.toggle("active");


        // Remove Active and Hide pannel for other elements previously opened
        var setClasses = !this.classList.contains("active");
        setClass(acc, 'active', 'remove');
        setClass(otherPanels, 'show', 'remove');

        var panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
            panel.style.maxHeight = null;
        } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
        }
    });
}

function setClass(els, className, fnName) {
    for (var i = 0; i < els.length; i++) {
        els[i].classList[fnName](className);
    }
}
