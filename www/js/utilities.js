function unhighlightMenu(name) {
    document.getElementById(name).style.borderRightStyle = "";
    document.getElementById(name).style.backgroundColor = "gainsboro";
}

function resetMenu() {
    unhighlightMenu("overview");
    unhighlightMenu("history");
    unhighlightMenu("settings");
}

function highlightMenu(name) {
    resetMenu();
    document.getElementById(name).style.borderRightStyle = "solid";
    document.getElementById(name).style.backgroundColor = "lightgrey";
}


