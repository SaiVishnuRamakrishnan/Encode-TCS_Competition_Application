var result_table = document.getElementById("result_table");
var test_case = ["Login", "Hotel Booking", "Flight Booking", "Car Booking"]

var xobj = new XMLHttpRequest();
xobj.overrideMimeType("application/json");
xobj.open("GET", "result.json", true);
xobj.onreadystatechange = function () {
    if (xobj.readyState == 4 && xobj.status == "200") {
        var json = JSON.parse(xobj.responseText)
        for (var j = 0; j < 4; j++) {
            var table_row = document.createElement("tr");
                var label = document.createElement("td"), status = document.createElement("td");
                var label_text = document.createTextNode(test_case[j]),status_text;
                if(json.result[j]===1){
                    status_text = document.createTextNode("Pass");
                }
                else{
                    status_text = document.createTextNode("Fail");
                }
                label.appendChild(label_text);
                status.appendChild(status_text);
                table_row.appendChild(label);
                table_row.appendChild(status);
                result_table.appendChild(table_row);
                console.log("hello")
        }
    }
}

xobj.send(null)

let canvas = document.getElementById("result-pie").getContext("2d");

var myPieChart = new Chart(canvas, {
    type: 'pie',
    data: [1,2,3,4],
});