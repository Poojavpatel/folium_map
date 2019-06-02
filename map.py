import folium

#create a map object
m=folium.Map(location=[12.971599,77.594566], zoom_start=13)

# generate html file corresponding this map
m.save('map.html')