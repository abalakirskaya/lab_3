import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl
import folium
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py
'''
This module saves geolocations of users` friends on the web-map('templates/Map.html')
'''
TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
def adress(city):
    geolocator = Nominatim(user_agent="specify_your_app_name")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
    try:
        for point in [city]:
            location = geolocator.geocode(point)
            return (location.latitude, location.longitude)
    except:
        return False
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
map = folium.Map(location=[48.314775, 25.082925], zoom_start=3)
fe = folium.FeatureGroup(name="Most popular cities")
while True:
    acct = input('Enter Twitter Account:')
    if (len(acct) < 1): break
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '20'})
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()

    js = json.loads(data)

    headers = dict(connection.getheaders())
    for u in js['users']:
        if not 'location' in u:
            pass
        else:
            location =u['location']
            name=u['screen_name']
            try:
                coord = adress(location)
                if coord:
                    lt = coord[0]
                    ln = coord[1]
                    fe.add_child(folium.CircleMarker(location=[lt, ln], radius=10, popup=str(name),
                                                 fill_color='red', fill_opacity=0.7))
            except:
                pass
    map.add_child(fe)
    map.save('templates/Map.html')
