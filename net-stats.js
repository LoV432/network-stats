function showData(){
fetch("./stats.json")
    .then(function (resp) {
        return resp.json();
    })
    .then(function (data) {
        document.getElementById("totaljava").innerHTML = data.TotalDomains;
        document.getElementById("blockedjava").innerHTML = data.BlockedDomains;
        percentGet = data.BlockedDomains/data.TotalDomains*100
        percentGet = Math.round(percentGet)
        document.getElementById("percentjava").innerHTML = percentGet+"%";
        document.getElementById("namejava").innerHTML = data.TopUser;
        var i = 0;
        for (x in data.AllowedDomainsList) {
            input = data.AllowedDomainsList[i]
            document.getElementsByClassName("a")[i].innerHTML = input[0];
            document.getElementsByClassName("am")[i].innerHTML = input[1];
            i++
        }
        var i = 0;
        for (x in data.BlockedDomainsList) {
            input = data.BlockedDomainsList[i]
            document.getElementsByClassName("b")[i].innerHTML = input[0];
            document.getElementsByClassName("bm")[i].innerHTML = input[1];
            i++
        }
        for (i = 0; i < 10; i++) {
            input = data.LastDomainsRequest[i]
            document.getElementsByClassName("rt")[i].innerHTML = input[2];
            document.getElementsByClassName("rd")[i].innerHTML = input[4];
            document.getElementsByClassName("ru")[i].innerHTML = input[5];
            document.getElementsByClassName("rs")[i].innerHTML = input[3];

        }
    });
}
function getData() {
    var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/cgi-bin/py.py", false);
    xhttp.send();
    showData();
}

function showRealTime() {
    document.getElementById("chart").style.visibility = "collapse";
    document.getElementById("real-time-list").style.visibility = "visible";
}

function showChart() {
	var xhttp = new XMLHttpRequest();
    xhttp.open("GET", "/cgi-bin/graph.py", false);
    xhttp.send();
    document.getElementById("real-time-list").style.visibility = "collapse";
    document.getElementById("chart-img").style.backgroundImage='url(img/img.png)';
    document.getElementById("chart").style.visibility = "visible";
}
window.addEventListener('load', function () {
getData();
})



