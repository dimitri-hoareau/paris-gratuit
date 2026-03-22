import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import "./Map.scss";

function Map() {
  const parisCenter = [48.8566, 2.3522];

  return (
    <div className="map">
      <MapContainer center={parisCenter} zoom={13} className="map__container">
        <TileLayer
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        <Marker position={parisCenter}>
          <Popup>Paris - Centre ville</Popup>
        </Marker>
      </MapContainer>
    </div>
  );
}

export default Map;
