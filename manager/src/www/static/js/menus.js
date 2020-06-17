// menus.js: contains functions for controlling what is displayed with each menu 
var current_tab = "NONE";  // current_tab indicates the current menu, by default it is "NONE"

// clearContent: clears the interior of the content <div>
function clearContent() {
    document.getElementById("content").innerHTML = "<br><br>";
}

// loadOverview: gets the node information from the webserver and displays it
function loadOverview(data) {
    // if already on the overview tab, no need to do anything
    if (current_tab != "overview") {
        // fetch the /nodes route (nodes information)
        fetch('/nodes').then(response => response.json())
        .then(data => {
            clearContent();  // clear the content of the content <div>
            loadNodes(data);  // load the node info boxes
            highlightMenu("overview");  // highlight the "overview" menu button
            current_tab = "overview";  // set the current tab variable
        })
        .catch(error => {
            console.log(error);  // if there is an error, log it!
        });
    }
}

// loadSettings: gets the settings information from the cookies/webserver and displays it
function loadSettings() {
    if (current_tab != "settings") {
        clearContent();  // clear the content of the content <div>
        generateSettings();  // load the settings box
        highlightMenu("settings");  // highlight the "settings" menu button
        current_tab = "settings";  // set the current tab variable
    }
}
