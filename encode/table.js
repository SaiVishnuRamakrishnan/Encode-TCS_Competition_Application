var result_table = document.getElementById("result_table");
var test_case = ["Login", "Hotel Booking", "Flight Booking", "Car Booking"];
var pass = 0, fail = 0;

var xobj = new XMLHttpRequest();
xobj.overrideMimeType("application/json");
xobj.open("GET", "result.json", true);
xobj.onreadystatechange = function () {
    if (xobj.readyState == 4 && xobj.status == "200") {
        var json = JSON.parse(xobj.responseText)
        for (var j = 0; j < 4; j++) {
            var table_row = document.createElement("tr");
            var label = document.createElement("td"), status = document.createElement("td");
            var label_text = document.createTextNode(test_case[j]), status_text;
            if (json.result[j] === 1) {
                status_text = document.createTextNode("Pass");
                pass++;
            }
            else {
                status_text = document.createTextNode("Fail");
                fail++;
            }
            label.appendChild(label_text);
            status.appendChild(status_text);
            table_row.appendChild(label);
            table_row.appendChild(status);
            result_table.appendChild(table_row);

        }
        Chart.defaults.global.defaultFontSize = 30;
        let canvas = document.getElementById("result-pie").getContext("2d");
        var myPieChart = new Chart(canvas, {
            type: 'pie',
            data: {
                labels: ['Pass', 'Fail'],
                datasets: [{
                    label: 'STATUS',
                    data: [pass, fail],
                    backgroundColor: ['rgba(0,229,76,0.8)', 'rgba(230,61,0,0.8)']
                }]
            }
        });
    }
}

xobj.send(null)

$(document).ready(function () {
    $.ajax({
        url: "sample.txt",
        dataType: "text",
        success: function (data) {
            // $(".text").html(data);
            document.querySelector('.log').innerHTML = data;
        }
    });
}); 
