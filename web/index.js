accessToken = 'pk.eyJ1IjoicHNtYWFhcm9uIiwiYSI6ImNqb25kMjcyaDE2am8zd2xzMnI4b2djeWwifQ.zrCz93IDztoB1Yq6ZBO1cw';
var map = new L.map('map');
map.setView([-27.3717673, 135.3515625], 4);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: accessToken
}).addTo(map);

$.ajax({
    type: "GET",
    url: "/api/getPoints",
    dataType: "json",
    success: function (response) {
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
            p.addTo(map);

        });
    }
});
