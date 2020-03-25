var current_tab = "NONE";

function clearContent() {
    document.getElementById("content").innerHTML = "<br><br>";
}

function loadOverview(data) {
    if (current_tab != "overview") {
        console.log("LoadOverview()");
        clearContent();
        loadNodes(data);
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
