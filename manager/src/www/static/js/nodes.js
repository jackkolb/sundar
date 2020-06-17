// nodes.js: contains functions for displaying node data in the "overview" viewspace

// generateNode: adds a new node tile to the node list
function generateNode(id, data) {
    // get the name of the node
    var node_name = data[id].name;
    
    // get the latest node damage from the node damage history
    if ("history" in data[id]) {
        console.log(data[id]["history"][1][1]);
        var bearing_status = data[id]["history"][data[id]["history"].length-1][1];
    }
    else {
        var bearing_status = NaN;
    }

    // get the life estimate of the node
    var estimate_life = data[id].life;

    // create a <div> for the node tile
    var node = document.createElement("div");
    node.className = "node-overview";

    // create a <div> container for the node title (name and indicator circle)
    var nodeStatus = document.createElement("div");
    nodeStatus.className = "node-status";

    // create a <div> for the node name
    var nodeName = document.createElement("div");
    nodeName.className = "node-name";
    nodeName.innerHTML = node_name + "<br>";

    // create a <div> for the damage indicator circle, change the color accordingly
    var nodeCircle = document.createElement("div");
    nodeCircle.className = "node-circle";
    var circleColor = "black";
    if (parseInt(bearing_status) <= 3) {
        circleColor = "green";
    }
    else if (parseInt(bearing_status) == 4) {
        circleColor = "gold";
    }
    else if (parseInt(bearing_status) == 5) {
        circleColor = "red";
    }
    nodeCircle.style.backgroundColor = circleColor;
    nodeCircle.style.boxShadow = "0 0 10px 0px " + circleColor;

    // create a <div> container for the node information (damage, life estimate, etc)
    var nodeInformation = document.createElement("div");
    nodeInformation.className = "node-information";

    // create a <div> for the node damage
    var nodeDamage = document.createElement("div");
    nodeDamage.className = "node-detail";
    nodeDamage.innerHTML = "Bearing Damage: " + bearing_status;

    // create a <div> for the node life estimate
    var nodeLife = document.createElement("div");
    nodeLife.className = "node-detail";
    nodeLife.innerHTML = "Life Estimate: " + estimate_life + " weeks";

    // create a line break
    var nodeBreak = document.createElement("br");
    nodeBreak.className = "node-detail";

    // create a <div> for the node IP address
    var nodeIP = document.createElement("div");
    nodeIP.className = "node-detail";
    nodeIP.innerHTML = "IP Address: " + data[id].ip;

    // create a <div> for the node serial
    var nodeSerial = document.createElement("div");
    nodeSerial.className = "node-detail";
    nodeSerial.innerHTML = "Serial: " + data[id].serial;

    // create a <div> for the node Speck information
    var nodeSpeck = document.createElement("div");
    nodeSpeck.className = "node-detail";
    nodeSpeck.innerHTML = "Speck: " + data[id].speck;

    // create a <div> for the node "last synced" timestamp
    var nodeTimestamp = document.createElement("div");
    nodeTimestamp.className = "node-detail";
    var timeStamp = Math.floor(Date.now() / 1000);
    nodeTimestamp.innerHTML = "Last Sync: " + String(timeStamp - Number(data[id].last_contact)) + " sec";

    // add the various information <div>'s to the overall node div, taking into account the settings of what to display
    node.appendChild(nodeStatus);
        nodeStatus.appendChild(nodeName);
        nodeStatus.appendChild(nodeCircle);
    node.appendChild(nodeInformation);
        if (getCookie("displayDamage") == "true") {
            nodeInformation.appendChild(nodeDamage);
        }
        if (getCookie("displayEstimate") == "true") {
            nodeInformation.appendChild(nodeLife);
        }
        nodeInformation.appendChild(nodeBreak);

        if (getCookie("displayAddress") == "true") {
            nodeInformation.appendChild(nodeIP);
        }
        if (getCookie("displaySerial") == "true") {
            nodeInformation.appendChild(nodeSerial);
        }
        if (getCookie("displaySpeck") == "true") {
            nodeInformation.appendChild(nodeSpeck);
        }
        if (getCookie("displaySync") == "true") {
            nodeInformation.appendChild(nodeTimestamp);
        }

    // when clicking on a node, the node's webserver will open in a new tab
    node.setAttribute("onclick", "window.open('http://" + data[id].ip + "');");
    node.setAttribute("target", "_blank");
    return node;
}

// addUL: adds a node tile to the node tile list
function addUL(node) {
    var list = document.getElementById("node-tiles");
    var newLI = document.createElement("li");
        newLI.className = "tile";
        newLI.appendChild(node);
    list.appendChild(newLI);
}

// loadNodes: loads the node tile list from the node data
function loadNodes(data) {
    var ul = document.createElement("ul");
        ul.id = "node-tiles";
        ul.className = "tile-list";
    document.getElementById("content").appendChild(ul);

    console.log(data);
    for (var key in data) {
        console.log(key);
        addUL(generateNode(key, data));
    }
}
