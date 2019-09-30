function initMap() {
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 12,
      center: {lat: 41.8781, lng: -87.6298}
    });
  
    var kmlLayer = new google.maps.KmlLayer({
      url: 'https://raw.githubusercontent.com/hmakinde/map_stuff/master/crimechicago.kml',
      suppressInfoWindows: true,
      map: map
    });
  
    kmlLayer.addListener('click', function(kmlEvent) {
      var text = kmlEvent.featureData.description;
      showInContentWindow(text);
    });
  
    function showInContentWindow(text2) {
      var sidediv = document.getElementById('capture');
      sidediv.innerHTML = text2;
    }
  }