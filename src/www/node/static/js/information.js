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
                        labelString: 'Date',
                        fontSize: 15
                    },
                    ticks: {
                        fontSize: 15
                    }
                }],
                yAxes: [{
                    display: true,
                    scaleLabel: {
                        display: true,
                        labelString: 'Bearing Damage Level',
                        fontSize: 15
                    },
                    ticks: {
                        beginAtZero: true,
                        stepSize: 1,
                        max: 5,
                        fontSize: 15
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

function setActive() {
    value = document.getElementById("activeToggle").checked;
    console.log("set active to " + value)
    sendUpdate("active", value)
}

function setFlashdrive() {
    value = document.getElementById("flashdriveToggle").checked;
    console.log("set flashdrive to " + value);
    sendUpdate("flashdrive", value);
}

function setDuration() {
    var value = document.getElementById("duration-entry").value;
    if (value == "" || value <= 0) {
        value = 20;
    }
    console.log("set duration to " + value);
    sendUpdate("duration", value);
}

function setRate() {
    var value = document.getElementById("rate-entry").value;
    if (value == "" || value <= 0) {
        value = 500;
    }
    console.log("set rate to " + value);
    sendUpdate("rate", value);
    return;
}

function setDelay() {
    var value = document.getElementById("delay-entry").value;
    if (value == "" || value <= 0) {
        value = 3600;
    }
    console.log("set delay to " + value);
    sendUpdate("delay", value);
    return;
}


function downloadLogs() {
    window.location.href = "/logs";
}

function downloadHistory() {
    fetch("/history")
    .then(resp=>resp.blob())
    .then(blob => {
      const url = window.URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.style.display = 'none';
      NOTSUREWHATTHISIS = 'history.data';
      document.body.appendChild(a);
      a.click();
      window.URL.revokeObjectURL(url);
    })
    .catch(() => alert('unable to download History'));
    return;
}

function downloadRawData() {
    window.location.href="/raw-data";
}

function downloadDailyData() {
    window.location.href="/daily-data";
}

function flashLEDs() {
    console.log("Flashing LEDs");
    sendUpdate("flashLED", "true");
    return;
}

function resetNode() {
    if (confirm("Are you sure you wish to reset the node? This will delete logs, history, and cannot be reversed!")) {
        if (confirm("Are you completely sure you wish to reset the node? This is the last confirmation.")) {
            setDefaults();
            sendUpdate("reset", "true");
        }
    }
}

function setDefaults() {
    var active_node = false;
    var default_duration = 20;
    var default_rate = 1000;
    var save_flashdrive = true;

    document.getElementById("activeToggle").checked = active_node;
    setActive();
    document.getElementById("duration-entry").value = default_duration;
    setDuration();
    document.getElementById("rate-entry").value = default_rate;
    setRate();
    document.getElementById("flashdriveToggle").checked = save_flashdrive;
    setFlashdrive();
    return;
}

function restartNode() {
    var url = "restart";
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", url, true);
    xmlHttp.send(null);
}

function sendUpdate(key, value) {
    var url = "update?key=" + key + "&value=" + value;
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open("GET", url, true);
    xmlHttp.send(null);
}

function getDamageColor(damage) {
    var color = "grey";
    if (damage == 5) {
        color = "red";
    }
    if (damage == 4) {
        color = "yellow";
    }
    if (damage == 3) {
        color = "yellow";
    }
    if (damage == 2) {
        color = "green";
    }
    if (damage == 1) {
        color = "green";
    }
    return color;
}