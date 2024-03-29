// create a map in the "map" div, set the view to a given place and zoom
var map = L.map('map').setView([47.2, -1.575], 14);

// add an OpenStreetMap tile layer
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

//get json content
$.getJSON("coordonnees.json", function(json) { // this will show the info it in firebug console
	for (var row in json) {
		// add a marker in the given location, attach some popup content to it and open the popup
		if (json[row].Latitude != '') //Do not handle entries with no geographical information
		{
			marker = L.marker([json[row].Latitude, json[row].Longitude]).addTo(map).bindPopup(json[row].Titre+"<br>"+json[row].Resume);
		}
	}
});

//Draw polygon representing mock-up bounds
var bounds = [[47.19447, -1.60970], [47.18908, -1.60863], [47.18599, -1.60611], [47.20479, -1.55415], [47.21052, -1.55556], [47.21317, -1.55857]];
L.polygon(bounds, {color: "#ff7800", weight: 5}).addTo(map);
