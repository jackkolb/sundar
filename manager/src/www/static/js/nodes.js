function generateNode(id, data) {
    var node_name = data[id].name;
    
    if ("history" in data[id]) {
        console.log(data[id]["history"][1][1]);
        var bearing_status = data[id]["history"][data[id]["history"].length-1][1];
    }
    else {
        var bearing_status = NaN;
    }
    var estimate_life = data[id].life;

    var node = document.createElement("div");
    node.className = "node-overview";

    var nodeStatus = document.createElement("div");
    nodeStatus.className = "node-status";

    var nodeName = document.createElement("div");
    nodeName.className = "node-name";
    nodeName.innerHTML = node_name + "<br>";

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

    var nodeInformation = document.createElement("div");
    nodeInformation.className = "node-information";

    var nodeDamage = document.createElement("div");
    nodeDamage.className = "node-detail";
    nodeDamage.innerHTML = "Bearing Damage: " + bearing_status;

    var nodeLife = document.createElement("div");
    nodeLife.className = "node-detail";
    nodeLife.innerHTML = "Life Estimate: " + estimate_life + " weeks";

    var nodeBreak = document.createElement("br");
    nodeBreak.className = "node-detail";

    var nodeIP = document.createElement("div");
    nodeIP.className = "node-detail";
    nodeIP.innerHTML = "IP Address: " + data[id].ip;

    var nodeSerial = document.createElement("div");
    nodeSerial.className = "node-detail";
    nodeSerial.innerHTML = "Serial: " + data[id].serial;

    var nodeSpeck = document.createElement("div");
    nodeSpeck.className = "node-detail";
    nodeSpeck.innerHTML = "Speck: " + data[id].speck;

    var nodeTimestamp = document.createElement("div");
    nodeTimestamp.className = "node-detail";
    var timeStamp = Math.floor(Date.now() / 1000);
    nodeTimestamp.innerHTML = "Last Sync: " + String(timeStamp - Number(data[id].last_contact)) + " sec";

    
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

    node.setAttribute("onclick", "window.open('http://" + data[id].ip + "');");
    node.setAttribute("target", "_blank");
    return node;
}

function addUL(node) {
    var list = document.getElementById("node-tiles");
    var newLI = document.createElement("li");
        newLI.className = "tile";
        newLI.appendChild(node);
    list.appendChild(newLI);
}

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