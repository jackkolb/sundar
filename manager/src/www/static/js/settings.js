// settings.js: contains functions for the settings panel of the manager webserver interface

// generateSettings: creates the graphical settings panel
function generateSettings() {
    // content is an empty <div> in the HTML page that is filled with page content
    var content = document.getElementById("content");

    // create the settings box, a panel that gets populated
    var settingsBox = document.createElement("div");
        settingsBox.className = "settings-box";
        settingsBox.id = "settings-box";

    // sync timer is an input for the node sync period
    var syncTimer = document.createElement("div");
        syncTimer.className = "settings-item";
        syncTimer.id = "sync-timer";
        var syncTimerLabel = document.createElement("div");
            syncTimerLabel.className = "settings-left";
            syncTimerLabel.innerHTML = "Node Sync Delay (sec)"
        var syncTimerEntry = document.createElement("input");
            syncTimerEntry.className = "settings-right numberbox";
            syncTimerEntry.id = "sync-timer-entry";
            syncTimerEntry.type = "number";
            syncTimerEntry.setAttribute("onchange", "setTimer();");
        syncTimer.appendChild(syncTimerLabel);
        syncTimer.appendChild(syncTimerEntry);
      
    // add a line break
    var breakline = document.createElement("br");

    // display damage is a toggle for whether the nodes' damages are displayed
    var displayDamage = document.createElement("div");
        displayDamage.className = "settings-item";
        displayDamage.id = "display-damage";
        var displayDamageText = document.createElement("div");
            displayDamageText.className = "settings-left";
            displayDamageText.innerHTML = "Display Nodes' Damage Level";
        var displayDamageSwitch = document.createElement("div");
            displayDamageSwitch.className = "settings-right";
            var displayDamageLabel = document.createElement("label");
                displayDamageLabel.className = "switch";
                var displayDamageInput = document.createElement("input");
                    displayDamageInput.type = "checkbox";
                    displayDamageInput.setAttribute("onclick", "setDisplayDamage()");
                    displayDamageInput.id = "damageToggle";
                var displayDamageSpan = document.createElement("span");
                    displayDamageSpan.className = "slider round";
                    displayDamageSpan.setAttribute("onhover", "console.log('adssad'); document.getElementById('display-damage').style.color = '#2196F3'");
                displayDamageLabel.appendChild(displayDamageInput);
                displayDamageLabel.appendChild(displayDamageSpan);
            displayDamageSwitch.appendChild(displayDamageLabel);
        displayDamage.appendChild(displayDamageText);
        displayDamage.appendChild(displayDamageSwitch);

    // display node life estimate is a toggle for whether the nodes' life estimate are displayed
    var displayEstimate = document.createElement("div");
        displayEstimate.className = "settings-item";
        displayEstimate.id = "display-estimate"
        var displayEstimateText = document.createElement("div");
            displayEstimateText.className = "settings-left";
            displayEstimateText.innerHTML = "Display Nodes' Life Estimate";
        var displayEstimateSwitch = document.createElement("div");
            displayEstimateSwitch.className = "settings-right";
            displayEstimateSwitch.setAttribute("onhover", "document.getElementById('display-estimate').style.color = '#2196F3'");
            var displayEstimateLabel = document.createElement("label");
                displayEstimateLabel.className = "switch";
                var displayEstimateInput = document.createElement("input");
                    displayEstimateInput.type = "checkbox";
                    displayEstimateInput.setAttribute("onclick", "setDisplayEstimate()");
                    displayEstimateInput.id = "estimateToggle";
                var displayEstimateSpan = document.createElement("span");
                    displayEstimateSpan.className = "slider round";
                displayEstimateLabel.appendChild(displayEstimateInput);
                displayEstimateLabel.appendChild(displayEstimateSpan);
            displayEstimateSwitch.appendChild(displayEstimateLabel);
        displayEstimate.appendChild(displayEstimateText);
        displayEstimate.appendChild(displayEstimateSwitch);

    // display node IP address is a toggle for whether the nodes' IP addresses are displayed
    var displayAddress = document.createElement("div");
        displayAddress.className = "settings-item";
        displayAddress.id = "display-address";
        var displayAddressText = document.createElement("div");
            displayAddressText.className = "settings-left";
            displayAddressText.innerHTML = "Display Nodes' IP Address";
        var displayAddressSwitch = document.createElement("div");
            displayAddressSwitch.className = "settings-right";
            displayAddressSwitch.setAttribute("onhover", "document.getElementById('display-address').style.color = '#2196F3'");
            var displayAddressLabel = document.createElement("label");
                displayAddressLabel.className = "switch";
                var displayAddressInput = document.createElement("input");
                    displayAddressInput.type = "checkbox";
                    displayAddressInput.setAttribute("onclick", "setDisplayAddress()");
                    displayAddressInput.id = "addressToggle";
                var displayAddressSpan = document.createElement("span");
                    displayAddressSpan.className = "slider round";
                displayAddressLabel.appendChild(displayAddressInput);
                displayAddressLabel.appendChild(displayAddressSpan);
            displayAddressSwitch.appendChild(displayAddressLabel);
        displayAddress.appendChild(displayAddressText);
        displayAddress.appendChild(displayAddressSwitch);
    
    // display speck is a toggle for whether the nodes' Speck information is displayed (see more about Speck at kolb.dev/speck)
    var displaySpeck = document.createElement("div");
        displaySpeck.className = "settings-item";
        displaySpeck.id = "display-speck";
        var displaySpeckText = document.createElement("div");
            displaySpeckText.className = "settings-left";
            displaySpeckText.innerHTML = "Display Nodes' Speck Information";
        var displaySpeckSwitch = document.createElement("div");
            displaySpeckSwitch.className = "settings-right";
            displaySpeckSwitch.setAttribute("onhover", "document.getElementById('display-speck').style.color = '#2196F3'");
            var displaySpeckLabel = document.createElement("label");
                displaySpeckLabel.className = "switch";
                var displaySpeckInput = document.createElement("input");
                    displaySpeckInput.type = "checkbox";
                    displaySpeckInput.setAttribute("onclick", "setDisplaySpeck()");
                    displaySpeckInput.id = "speckToggle";
                var displaySpeckSpan = document.createElement("span");
                    displaySpeckSpan.className = "slider round";
                displaySpeckLabel.appendChild(displaySpeckInput);
                displaySpeckLabel.appendChild(displaySpeckSpan);
            displaySpeckSwitch.appendChild(displaySpeckLabel);
        displaySpeck.appendChild(displaySpeckText);
        displaySpeck.appendChild(displaySpeckSwitch);

    // display serial is a toggle for whether the nodes' serial number is displayed
    var displaySerial = document.createElement("div");
        displaySerial.className = "settings-item";
        displaySerial.id = "display-serial"
        var displaySerialText = document.createElement("div");
            displaySerialText.className = "settings-left";
            displaySerialText.innerHTML = "Display Nodes' Serial Information";
        var displaySerialSwitch = document.createElement("div");
            displaySerialSwitch.className = "settings-right";
            displaySerialSwitch.setAttribute("onhover", "document.getElementById('display-serial').style.color = '#2196F3'");
            var displaySerialLabel = document.createElement("label");
                displaySerialLabel.className = "switch";
                var displaySerialInput = document.createElement("input");
                    displaySerialInput.type = "checkbox";
                    displaySerialInput.setAttribute("onclick", "setDisplaySerial()");
                    displaySerialInput.id = "serialToggle";
                var displaySerialSpan = document.createElement("span");
                    displaySerialSpan.className = "slider round";
                displaySerialLabel.appendChild(displaySerialInput);
                displaySerialLabel.appendChild(displaySerialSpan);
            displaySerialSwitch.appendChild(displaySerialLabel);
        displaySerial.appendChild(displaySerialText);
        displaySerial.appendChild(displaySerialSwitch);

    // display sync is a toggle for whether the time since last sync is displayed
    var displaySync = document.createElement("div");
        displaySync.className = "settings-item";
        displaySync.id = "display-sync"
        var displaySyncText = document.createElement("div");
            displaySyncText.className = "settings-left";
            displaySyncText.innerHTML = "Display Nodes' Last Sync Counter";
        var displaySyncSwitch = document.createElement("div");
            displaySyncSwitch.className = "settings-right";
            displaySyncSwitch.setAttribute("onhover", "document.getElementById('display-sync').style.color = '#2196F3'");
            var displaySyncLabel = document.createElement("label");
                displaySyncLabel.className = "switch";
                var displaySyncInput = document.createElement("input");
                    displaySyncInput.type = "checkbox";
                    displaySyncInput.setAttribute("onclick", "setDisplaySync()");
                    displaySyncInput.id = "syncToggle";
                var displaySyncSpan = document.createElement("span");
                    displaySyncSpan.className = "slider round";
                displaySyncLabel.appendChild(displaySyncInput);
                displaySyncLabel.appendChild(displaySyncSpan);
            displaySyncSwitch.appendChild(displaySyncLabel);
        displaySync.appendChild(displaySyncText);
        displaySync.appendChild(displaySyncSwitch);

    // add each of these components to the settings box to populate the panel
    settingsBox.appendChild(syncTimer);
    settingsBox.appendChild(breakline);
    settingsBox.appendChild(displayDamage);
    settingsBox.appendChild(displayEstimate);
    settingsBox.appendChild(displayAddress);
    settingsBox.appendChild(displaySpeck);
    settingsBox.appendChild(displaySerial);
    settingsBox.appendChild(displaySync);

    // make a button for adding a new node to the network
    var addNodeButton = document.createElement("button");
        addNodeButton.className = "add-node-button";
        addNodeButton.id = "add-node-button";
        addNodeButton.innerHTML = "(+) Add Node";
        addNodeButton.setAttribute("onclick", "showNewNodeEntry()");

    // a text field for entering the IP address when adding a new node to the network (initially hidden)
    var newNodeEntry = document.createElement("input");
        newNodeEntry.className = "new-node-entry text-entry";
        newNodeEntry.id = "node-text-entry"
        newNodeEntry.type = "text";
        newNodeEntry.placeholder = "New Node IP Address";
        newNodeEntry.setAttribute("visibility", "hidden");
        newNodeEntry.setAttribute("onchange", "addNodeIP()");

    // add the "add node" button and the "new node IP address" entry to the settings box
    settingsBox.appendChild(addNodeButton);
    settingsBox.appendChild(newNodeEntry);

    // make a table to show all of the currently registered nodes
    var nodeTable = document.createElement("table");
        nodeTable.id = "nodeTable";
        nodeTable.className = "settings-node-table";
    
    // add the table to the settings box
    settingsBox.appendChild(nodeTable);

    // populate the table with the nodes
    loadNodeSeries();

    // add the settings box to the content <div>
    content.appendChild(settingsBox);

    // initially hide the new node IP address input box
    hideNewNodeEntry();

    // get the current sync timer period from the webserver's saved settings
    getTimer();

    // by default, have all settings displayed
    displayDamageInput.checked = (getCookie("displayDamage") == "true");
    displayEstimateInput.checked = (getCookie("displayEstimate") == "true");
    displayAddressInput.checked = (getCookie("displayAddress") == "true");
    displaySpeckInput.checked = (getCookie("displaySpeck") == "true");
    displaySerialInput.checked = (getCookie("displaySerial") == "true");
    displaySyncInput.checked = (getCookie("displaySync") == "true");
}

// showNewNodeEntry: shows the IP Address entry for adding a new node
function showNewNodeEntry() {
    document.getElementById("node-text-entry").style.visibility = "visible";
}

// hideNewNodeEntry: hides the IP address entry for adding a new node
function hideNewNodeEntry() {
    document.getElementById("node-text-entry").style.visibility = "hidden";
}

// errorAddNode: if there is an error (caused by not being able to reach the target IP address),
// change the add new node button to red and display an error message for 1 second
function errorAddNode() {
    var button = document.getElementById("add-node-button");
    button.style.color = "red";
    button.style.borderColor = "red";
    button.innerHTML = "Invalid address";
    window.setTimeout(function() {
        resetAddNodeButton();
    }, 1000);
}

// resetAddNodeButton: resets the add new node button to a default "add node"
function resetAddNodeButton() {
    var button = document.getElementById("add-node-button");
    button.style.color = "#2196F3";
    button.style.borderColor = "#2196F3";
    button.innerHTML = "(+) Add Node";
}

// loadingAddNodeButton: when adding to a new node, the "add node" button changes to a "connecting" message
function loadingAddNodeButton() {
    var button = document.getElementById("add-node-button");
    button.style.color = "purple";
    button.style.borderColor = "purple";
    button.innerHTML = "Connecting to Node";
}

// successAddNodeButton: when a new node is successfully added, the "add node" button changes to a "success" message
function successAddNodeButton() {
    var button = document.getElementById("add-node-button");
    button.style.color = "green";
    button.style.borderColor = "green";
    button.innerHTML = "Success!";
}

// addNodeIP: adds a new node using the IP address given, and displays information about the process as it
// connects to the node and succeeds/fails to add it to the network
function addNodeIP() {
    console.log("adding node");
    var ip = document.getElementById("node-text-entry").value;
    document.getElementById("node-text-entry").value = "";
    loadingAddNodeButton();
    fetch("/add-node?ip=" + ip).then(response => response.json())
    .then(data => {
        console.log(data["result"]);
        if (data["result"] == "failure") {
            errorAddNode();
            hideNewNodeEntry();
        }
        else {
            successAddNodeButton();
            window.setTimeout(function() {loadNodeSeries(); resetAddNodeButton();}, 250);
        }
    }).catch(error => {
        console.log(error);
        errorAddNode();
        hideNewNodeEntry();
        window.setTimeout(function() {loadNodeSeries();}, 250);
    }); 
}

// generateNodeListing: adds a new entry to the node information table
function generateNodeListing(serial, name, ip) {
    var newListing = document.createElement("tr");
        var newListingSerial = document.createElement("td");
            newListingSerial.className = "settings-node-table-serial";
            newListingSerial.innerHTML = serial;
        var newListingName = document.createElement("td");
            newListingName.className = "settings-node-table-name";
            newListingName.innerHTML = name;
        var newListingIP = document.createElement("td");
            newListingIP.className = "settings-node-table-ip";
            newListingIP.innerHTML = ip;
        var newListingButtonHolder = document.createElement("td");
            newListingButtonHolder.className = "settings-node-table-buttonholder";
            var newListingButton = document.createElement("button");
                newListingButton.className = "settings-node-table-button"
                newListingButton.setAttribute("onclick", "removeSerial('" + serial + "')");
                newListingButton.innerHTML = "x";
            newListingButtonHolder.append(newListingButton);
        newListing.append(newListingSerial);
        newListing.append(newListingName);
        newListing.append(newListingIP);
        newListing.append(newListingButtonHolder);
    
    return newListing;
}

// removeSerial: removes a node by its serial number
function removeSerial(serial) {
    r = window.confirm("Are you sure you want to remove the node " + serial + "?")
    if (r) {
        fetch("/remove-serial?serial=" + serial);
        window.setTimeout(function() {loadNodeSeries();}, 250);
    }
}

// loadNodeSeries: loads the network's nodes from the webserver
function loadNodeSeries() {
    fetch('/nodes').then(response => response.json())
    .then(data => {
        document.getElementById("nodeTable").innerHTML = "";
        for (i in Object.keys(data)) {
            var serial = Object.keys(data)[i]
            var name = data[serial].name;
            var ip = data[serial].ip;
            var newListing = generateNodeListing(serial, name, ip);
            document.getElementById("nodeTable").append(newListing);
        }
    })
    .catch(error => {
        console.log(error);
    });    
}

// getTimer: gets the sync timer period from the webserver
function getTimer() {
    fetch("/get-sync").then(response => response.json())
    .then(data => {
        document.getElementById("sync-timer-entry").value = data;
    });
    return;
}

// setTimer: sets the sync timer period with the webserver
function setTimer() {
    var value = document.getElementById("sync-timer-entry").value;
    fetch("/set-sync?timer=" + value);
    return;
}

// setCookie: adds a new cookie
function setCookie(key, value) {
    var now = new Date();
    var expireTime = now.getTime() + 100000*43200;
    now.setTime(expireTime);
    document.cookie = key + '=' + value + ';expires='+now.toGMTString()+';path=/';
    return;
}

// getCookie: gets a specific cookie
function getCookie(key) {
    var name = key + "=";
    var decodedCookie = decodeURIComponent(document.cookie);
    var cookie_array = decodedCookie.split(';');
    for(var i = 0; i <cookie_array.length; i++) {
        var cookie = cookie_array[i];
        while (cookie.charAt(0) == ' ') {
            cookie = cookie.substring(1);
        }
        if (cookie.indexOf(name) == 0) {
            return cookie.substring(name.length, cookie.length);
        }
    }
    return "";
}

// setDisplayDamage: sets a cookie for showing the display damage
function setDisplayDamage() {
    var value = document.getElementById("damageToggle").checked;
    setCookie("displayDamage", value);
    return;
}

// setDisplayEstimate: sets a cookie for showing the nodes' damage estimates
function setDisplayEstimate() {
    var value = document.getElementById("estimateToggle").checked;
    setCookie("displayEstimate", value);
    return;
}

// setDisplayAddress: sets a cookie for showing the nodes' IP addresses
function setDisplayAddress() {
    var value = document.getElementById("addressToggle").checked;
    setCookie("displayAddress", value);
    return;
}

// setDisplaySpeck: sets a cookie for showing the nodes' speck information
function setDisplaySpeck() {
    var value = document.getElementById("speckToggle").checked;
    setCookie("displaySpeck", value);
    return;
}

// setDisplaySerial: sets a cookie for showing the nodes' serial information
function setDisplaySerial() {
    var value = document.getElementById("serialToggle").checked;
    setCookie("displaySerial", value);
    return;
}

// setDisplaySync: sets a cookie for showing the nodes' sync timers
function setDisplaySync() {
    var value = document.getElementById("syncToggle").checked;
    setCookie("displaySync", value);
    return;
}
