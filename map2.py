import pandas as pd
import folium
import os
import json

url = 'https://raw.githubusercontent.com/Poojavpatel/folium_map/master/datasets/data.csv'
df = pd.read_csv(url)

#create a map object
m=folium.Map(location=[12.971599,77.594566], zoom_start=12)

#pandas preprocessing and analysis
df.dropna(subset=['from_lat','from_long','to_lat','to_long'],inplace = True)
df1=pd.DataFrame(columns=["a","b","c","d"])
df1=df[['from_lat','from_long','to_lat','to_long']]
locations = df1.values.tolist()
# len(locations) is 34293

for loc in locations[0:200]:
    folium.Marker(location=[ loc[0], loc[1] ],icon=folium.Icon(color="blue",icon_color='white',icon='taxi',prefix='fa')).add_to(m)
    folium.Marker(location=[ loc[2], loc[3] ],icon=folium.Icon(color="red",icon_color='white',icon='taxi',prefix='fa')).add_to(m)

m.save('map2.html')