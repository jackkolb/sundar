// utilities.js: contains utility formatting functions used by the webpage 

// unhighlightMenu: removes the highlight border from the selected menu option
function unhighlightMenu(name) {
    document.getElementById(name).style.borderRightStyle = "";
    document.getElementById(name).style.backgroundColor = "gainsboro";
}

// resetMenu: removes the highlights from both the menu options
function resetMenu() {
    console.log("reset menu");
    unhighlightMenu("overview");
    unhighlightMenu("settings");
}

// highlightMenu: adds the highlight border to the selected menu option
function highlightMenu(name) {
    resetMenu();
    document.getElementById(name).style.borderRightStyle = "solid";
    document.getElementById(name).style.backgroundColor = "lightgrey";
}
