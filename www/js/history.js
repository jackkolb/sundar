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

function addSelectItem(name, id) {
    var selectTag = document.getElementById("history-select-tag");
    var newOption = document.createElement("option");
        newOption.setAttribute("value", id);
        newOption.innerHTML = name;
    selectTag.appendChild(newOption);
}

function generateHistory() {
    // create selection box
    var content = document.getElementById("content");
    var selectionBox = document.createElement("div");
        selectionBox.className = "selection-box"
    var selectionPanel = document.createElement("div");
        selectionPanel.className = "selection-panel";
    var historySelect = document.createElement("div");
        historySelect.className = "history-select";
    var selectTag = document.createElement("select");
        selectTag.id = "history-select-tag";
    historySelect.appendChild(selectTag);
    selectionPanel.appendChild(historySelect);
    selectionBox.appendChild(selectionPanel);
    content.appendChild(selectionBox);
    addSelectItem("Select Node:", 0);
    addSelectItem("Fume Hood A", 1);
    addSelectItem("Fume Hood B", 2);
    addSelectItem("Fume Hood C", 3);
    historySelectBox();



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