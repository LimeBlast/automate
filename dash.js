var dash_button = require('node-dash-button');
var spawn = require("child_process").spawn;

var goodnight = "ac:63:be:39:43:68", // Nescafe Dolce Gusto
    lunch = "ac:63:be:7c:60:90", // Biona Organic
    armchair = "ac:63:be:7b:85:8c", // Right Guard
    desk = "0c:47:c9:e7:46:e5"; // Fiesta kitchen towel

var buttons = [goodnight, lunch, armchair, desk];

var dash = dash_button(buttons, null, null, 'all'); //address from step above

dash.on("detected", function (dash_id) {
    var process;

    if (dash_id === goodnight) {
        console.log("goodnight was pressed");
        process = spawn('python3', ["/home/pi/Code/automate/goodnight.py"]);
    } else if (dash_id === lunch) {
        console.log("lunch was pressed");
        process = spawn('python3', ["/home/pi/Code/automate/lunch.py"]);
    } else if (dash_id === armchair) {
        console.log("armchair was pressed");
        process = spawn('python3', ["/home/pi/Code/automate/armchair.py"]);
    } else if (dash_id === desk) {
        console.log("desk was pressed");
        process = spawn('python3', ["/home/pi/Code/automate/desk.py"]);
    }

    // http://stackoverflow.com/a/23452742/1049688
    process.stdout.on('data', function (data) {
        console.log(data.toString());
    });
});
