// create a map in the "map" div, set the view to a given place and zoom
var map = L.map('map').setView([47.2, -1.575], 14);

// add an OpenStreetMap tile layer
L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

//get json content
markerarray=[];
$.getJSON("coord.json", function(json) { // this will show the info it in firebug console
	for (var row in json) {
		// add a marker in the given location, attach some popup content to it and open the popup
		marker = L.marker([json[row].Latitude, json[row].Longitude]).addTo(map).bindPopup(json[row].Titre+"<br>"+json[row].Resume);
		markerarray.push(marker);
	}
});

//get json content from modified historical sheets
$.getJSON("coord_new.json", function(json_new) { // this will show the info it in firebug console
	for (var row in json_new) {
		// verify the marker doesn't already exists
		var i;
		var test = false;
		for (i = 0; i < markerarray.length; i++) {
			if (markerarray[i].getLatLng().lat == json_new[row].Latitude && markerarray[i].getLatLng().lng == json_new[row].Longitude) {
				test = true;
				break;
			}
		}
		if (test == false) {
			L.marker([json_new[row].Latitude, json_new[row].Longitude]).addTo(map).bindPopup(json_new[row].Titre);
		}
	}
});
//Draw polygon representing mock-up bounds
var bounds = [[47.19447, -1.60970], [47.18908, -1.60863], [47.18599, -1.60611], [47.20479, -1.55415], [47.21052, -1.55556], [47.21317, -1.55857]];
L.polygon(bounds, {color: "#ff7800", weight: 5}).addTo(map);
