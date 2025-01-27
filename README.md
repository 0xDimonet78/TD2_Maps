# Mapa de Geolocalizaciones

Este mapa muestra las ubicaciones geográficas de varios puntos de interés.

## Mapa Interactivo

<div id="map" style="width: 100%; height: 500px;"></div>

<script>
// Incluir la librería Leaflet desde un CDN
document.write('<link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />');
document.write('<script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"><\/script>');

// Espera a que el DOM esté completamente cargado
document.addEventListener('DOMContentLoaded', function() {
  // Crear el mapa centrado en las coordenadas iniciales
  var map = L.map('map').setView([40.416775, -3.703790], 6);

  // Añadir una capa de mapas desde OpenStreetMap
  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
  }).addTo(map);

  // Añadir marcadores desde el archivo locations.js
  const locations = [
    { lat: 40.416775, lng: -3.703790, name: "Madrid" },
    { lat: 41.387917, lng: 2.169919, name: "Barcelona" },
    // más ubicaciones...
  ];

  locations.forEach(function(location) {
    L.marker([location.lat, location.lng]).addTo(map)
      .bindPopup(location.name);
  });
});
</script>
