var current_tab = "NONE";

function clearContent() {
    document.getElementById("content").innerHTML = "<br><br>";
}

function loadOverview(data) {
    if (current_tab != "overview") {
        fetch('/nodes').then(response => response.json())
        .then(data => {
            clearContent();
            loadNodes(data);
            highlightMenu("overview");
            current_tab = "overview";
        })
        .catch(error => {
            console.log(error);
        });
    }
}

function loadSettings() {
    if (current_tab != "settings") {
        clearContent();
        generateSettings();
        highlightMenu("settings");
        current_tab = "settings";
    }
}
