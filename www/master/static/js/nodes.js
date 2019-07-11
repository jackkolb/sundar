function generateNode(id, data) {
    console.log("TEST");
    var node_name = data[id].settings.name;
    console.log(data[id]["data"][1][1]);
    var bearing_status = data[id]["data"][data[id]["data"].length-1][1];
    var estimate_life = data[id].life;

    var node = document.createElement("div");
    node.className = "node-overview";

    var nodeName = document.createElement("div");
    nodeName.className = "node-name";
    nodeName.innerHTML = node_name;

    var nodeStatus = document.createElement("div");
    nodeStatus.className = "node-status";

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
    nodeDamage.className = "node-damage";
    nodeDamage.innerHTML = "Bearing Damage: " + bearing_status;

    var nodeLife = document.createElement("div");
    nodeLife.className = "node-life";
    nodeLife.innerHTML = "Life Estimate: " + estimate_life + " weeks";

    node.append(nodeName);
    node.append(nodeStatus);
        nodeStatus.append(nodeCircle);
    node.append(nodeInformation);
        nodeInformation.append(nodeDamage);
        nodeInformation.append(nodeLife);

    node.setAttribute("onclick", "loadHistory(); loadSelectedItem(" + id + ")");

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
    document.getElementById("content").append(ul);

    console.log("Hello");
    console.log(data);
    console.log("..");
    for (var key in data) {
        console.log(key)
        addUL(generateNode(key, data));
    }

}