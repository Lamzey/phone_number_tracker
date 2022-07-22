from unittest import result
import phonenumbers
from text import number
from phonenumbers import geocoder
from phonenumbers import carrier
import opencage
from opencage.geocoder import OpenCageGeocode
import folium


ch_number = phonenumbers.parse(number)
location = geocoder.description_for_number(ch_number, "en")
print(location)

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

key = '874152d605e945e7984d6d342d218679'

geocoder = OpenCageGeocode(key)
query = location
results = geocoder.geocode(query)
lng = results[0]['geometry']['lng']
lat = results[0]['geometry']['lat']
country = results[0]['components']['country_code']
an = results[0]['annotations']['timezone']['name']

print(lng, lat, country, an)

location = lng, lat

map = folium.Map(location=[lng, lat], zoom_start=10)
folium.Marker([lng, lat], popup=location).add_to(map)

map.save("m.html")