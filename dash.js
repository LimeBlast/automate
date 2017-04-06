var dash_button = require('node-dash-button');
var spawn = require("child_process").spawn;

var goodnight = "ac:63:be:39:43:68"; // Nescafe Dolce Gusto

var dash = dash_button([goodnight, "2e:3f:20:33:54:22"], null, null, 'all'); //address from step above
dash.on("detected", function (dash_id) {
    if (dash_id === goodnight) {
        console.log("goodnight was pressed");
        var process = spawn('python3', ["/home/pi/Code/automate/goodnight.py"]);
        // http://stackoverflow.com/a/23452742/1049688
        process.stdout.on('data', function (data) {
            console.log(data.toString());
        });
    } else if (dash_id === "2e:3f:20:33:54:22") {
        console.log("found the other!");
    }
});
