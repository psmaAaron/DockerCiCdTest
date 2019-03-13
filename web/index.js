accessToken = 'pk.eyJ1IjoicHNtYWFhcm9uIiwiYSI6ImNqb25kMjcyaDE2am8zd2xzMnI4b2djeWwifQ.zrCz93IDztoB1Yq6ZBO1cw';

let layerGroup = L.layerGroup();

let loadMap = () => {
    var map = new L.map('map');
    map.setView([-27.3717673, 135.3515625], 4);

    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        maxZoom: 18,
        id: 'mapbox.streets',
        accessToken: accessToken
    }).addTo(map);
    layerGroup.addTo(map);
    return map;
}

let populateMap = (map) => {
    $.ajax({
        type: "GET",
        url: "/api/point",
        dataType: "json",
        success: function (response) {
            layerGroup.clearLayers();
            response.forEach(point => {
                let p = L.geoJSON(point)

                var d = new Date(0); // The 0 there is the key, which sets the date to the epoch
                d.setUTCSeconds(point.properties.dttm);

                let popup = $("<div>");
                popup.append(
                    $("<p>").text(point.properties.message)
                );
                popup.append(
                    $("<p>")
                    .text("Added by " + point.properties.user + " on " + d.toLocaleDateString())
                    .addClass("smaller")
                );

                p.bindPopup(popup.html());
                p.addTo(layerGroup);

            });
        }
    });
}

let map = loadMap();
populateMap(map);
window.setInterval(function(){
    populateMap(map);
  }, 200);

map.on('click', (e) => {
    $.ajax({
        type: "POST",
        url: "/api/point",
        data: JSON.stringify({"lat": e.latlng.lat, "lng": e.latlng.lng}),
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        success: function (response) {
            populateMap(map);
        }
    })
});
