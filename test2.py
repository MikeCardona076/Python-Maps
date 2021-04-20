from geopy.geocoders import Nominatim
import folium as fm

geolocator = Nominatim(user_agent="mike")

location1 = geolocator.geocode("Altiplano, tijuana")
location2 = geolocator.geocode("Cerro colorado, tijuana")

print(location1.address)

mapa_mike = fm.Map(location=[location1.latitude,location1.longitude],
            )

fm.Marker([location1.latitude,location1.longitude], tooltip="Usted esta aqui").add_to(mapa_mike)
fm.Marker([location2.latitude,location2.longitude], tooltip="Destino").add_to(mapa_mike)

mapa_mike