from geopy.geocoders import Nominatim
import folium as fm

geolocator = Nominatim(user_agent="mike")

location = geolocator.geocode("Santa prisca, Taxco")
print(location.address)

mapa_mike = fm.Map(location=[location.latitude,location.longitude],
            zoom_start=20)

fm.Marker([location.latitude,location.longitude], tooltip="Usted esta aqui").add_to(mapa_mike)

mapa_mike