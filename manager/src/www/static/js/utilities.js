function unhighlightMenu(name) {
    document.getElementById(name).style.borderRightStyle = "";
    document.getElementById(name).style.backgroundColor = "gainsboro";
}

function resetMenu() {
    console.log("reset menu");
    unhighlightMenu("overview");
    unhighlightMenu("settings");
}

function highlightMenu(name) {
    resetMenu();
    document.getElementById(name).style.borderRightStyle = "solid";
    document.getElementById(name).style.backgroundColor = "lightgrey";
}


