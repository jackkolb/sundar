var current_tab = "NONE";

function clearContent() {
    document.getElementById("content").innerHTML = "<br><br>";
}

function loadOverview() {
    if (current_tab != "overview") {
        clearContent();
        loadNodes();
        highlightMenu("overview");
        current_tab = "overview";
    }
}

function loadHistory() {
    if (current_tab != "history") {
        clearContent();
        generateHistory();
        highlightMenu("history");
        current_tab = "history";
    }
}
