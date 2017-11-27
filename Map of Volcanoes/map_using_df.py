import folium
import pandas as pd

data = pd.read_csv('Volcanoes_USA.txt')

#lat = list(data['LAT'])
#lon = list(data['LON'])
#elev = list(data['ELEV'])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location = [43.650484, -79.403102], zoom_start = 6, tiles = 'Mapbox Bright', )

fgv = folium.FeatureGroup(name='Volcanoes')

for i in range(len(data)):
    folium.CircleMarker(location = [data['LAT'][i], data['LON'][i]], popup=str(data["ELEV"][i]) + ' m',  color = 'grey', fill = True, fill_color = color_producer(data["ELEV"][i]), fill_opacity = 1).add_to(fgv)

fgp = folium.FeatureGroup(name='Population')

fgp.add_child(folium.GeoJson(data = open('world.json', 'r', encoding = 'utf-8-sig').read(), style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save('Map2.html')
