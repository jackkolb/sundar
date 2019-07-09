function generatePlot(name, x_data, y_data) {
    // generate the plot
    var config = {
        type: 'line',
        data: {
            labels: x_data,
            datasets: [{
                borderColor: window.chartColors.blue,
                data: y_data,
                lineTension: 0
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            animation: {
                duration: 800
            },
            legend: {
                display: false
            },
            tooltips: {
                mode: 'index',
                intersect: false,
                displayColors: false
            },
            hover: {
                mode: 'nearest',
                intersect: true
            },
            scales: {
                xAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Date'
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Bearing Damage Level'
                    },
                    ticks: {
                        beginAtZero: true,
                        stepSize: 1,
                        max: 5
                    }                 
                }]
            }
        }
    };

    var plot_div = document.getElementById("history-plot");
        plot_div.innerHTML = "";
    var canvas = document.createElement("canvas");
    plot_div.appendChild(canvas);

    var ctx = canvas.getContext('2d');
    window.myLine = new Chart(ctx, config);
}

function generateHistory() {
    var content = document.getElementById("content");

    // create history
    var historyBox = document.createElement("div");
        historyBox.className = "history-box"
    var historyPanel = document.createElement("div");
        historyPanel.className = "history-panel";
    historyBox.appendChild(historyPanel);

    var historyName = document.createElement("div");
        historyName.className = "history-name";
        historyName.id = "history-name";
    var historyLife = document.createElement("div");
        historyLife.className = "history-life";
        historyLife.id = "history-life";
    var historyDamage = document.createElement("div");
        historyDamage.className = "history-damage";
        historyDamage.id = "history-damage";
    var historyPlot = document.createElement("div");
        historyPlot.className = "history-plot";
        historyPlot.id = "history-plot";

    historyPanel.appendChild(historyName);
    historyPanel.appendChild(historyLife);
    historyPanel.appendChild(historyDamage);
    historyPanel.appendChild(historyPlot);

    content.appendChild(historyBox);
}

function loadSelectedItem(id) {
    document.getElementById("history-name").innerHTML = data[id].name;
    document.getElementById("history-damage").innerHTML = "Bearing Damage Level: " + data[id].damage;
    document.getElementById("history-life").innerHTML = "Estimated Life: " + data[id].life + " weeks";

    data_x = [];
    data_y = [];
    for (var i = 0; i < data[id].data.length; i++) {
        var point = data[id].data[i];
        data_x.push(point[0]);
        data_y.push(point[1]);
    }

    generatePlot(data[id].name, data_x, data_y);
}

function generateNode(id) {
    var node_name = data[id].name;
    var bearing_status = data[id].damage;
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