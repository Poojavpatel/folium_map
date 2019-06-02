import folium
import os
import json

#create a map object
m=folium.Map(location=[12.971599,77.594566], zoom_start=12)

# vega data - load from json file
vis = os.path.join('datasets','vis.json')

folium.Marker([12.97,77.69],
              popup="<strong>Location 1</strong>",
              tooltip="Click for more Info"
              ).add_to(m)

folium.Marker([13.03,77.55],
              popup="<strong>Location 2</strong>",
              tooltip="Click for more Info",
              icon=folium.Icon(icon='cloud')
              ).add_to(m)
folium.Marker([12.92,77.67],
              popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)),
              width=450,height=250)),
              ).add_to(m)


# generate html file corresponding this map
m.save('map.html')