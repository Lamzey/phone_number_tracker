from unittest import result
import phonenumbers
from phone_number import number
from phonenumbers import geocoder

Key = '874152d605e945e7984d6d342d218679'

lamNumber = phonenumbers.parse(number)
yourLocation = geocoder.description_for_number(lamNumber, 'en')
print(yourLocation)

from phonenumbers import carrier

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, 'en'))

from opencage.geocoder import OpenCageGeocode
geocoder = OpenCageGeocode(Key)
query = str(yourLocation)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']

lng = results[0]['geometry']['lng']

country = results[0]['annotations']['timezone']['name']

print(lat, lng, country)

import folium

myMap = folium.Map(location=[lat, lng], zoom_start=5)
folium.Marker([lat, lng], popup=yourLocation).add_to(myMap)

myMap.save("mylocation.html")