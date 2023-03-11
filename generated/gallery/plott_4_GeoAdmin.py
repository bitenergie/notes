# -*- coding: utf-8 -*-
"""
GeoAdmin API

===================================

[Documentation](https://api3.geo.admin.ch/index.html)

[Intro in Rest API Real Python](https://realpython.com/api-integration-in-python/#rest-architecture)

Layers Metadata[¶](https://api3.geo.admin.ch/services/sdiservices.html#layers-metadata "Permalink to this headline")

This service provides metadata for all the available layers in the GeoAdmin API.
"""


# %%
import requests
from pprint import pprint

api_url = "https://api3.geo.admin.ch/rest/services/api/MapServer"
response = requests.get(api_url)
layers = response.json()

pprint(layers.keys())
print(len(layers["layers"]))

# %% [markdown]
# ## Search Layer by name

# %%
# search for layer url with text


param = {"searchText": "solar"}
response = requests.get("https://api3.geo.admin.ch/rest/services/api/MapServer?", param)
json = response.json()

name = json["layers"][0]["name"] 
full_name = json["layers"][0]["fullName"] 
link = json["layers"][0]["attributes"]["urlDetails"]

print(f"Name: {name}, \n Voller Name: {full_name} \n link: {link}")


# %%
# Get the egid  of building from address
street = 'Stadthausquai'
num = '17'
plz = '8001'
place = 'Zürich'


def feature_id(search_text):
    search_url = "https://api3.geo.admin.ch/rest/services/api/SearchServer?searchText=&origins=address&type=locations"
    search_value = {
    "searchText": search_text,
    }
    r = requests.get(search_url, params=search_value)
    results = r.json()
    pprint(results)

search_txt = f"{street} {num} {place} {plz}"
param = {"searchText": search_txt}


response = requests.get("https://api3.geo.admin.ch/rest/services/api/SearchServer?&origins=address&type=locations", param)
json = response.json()

detail = json["results"][0]["attrs"]["detail"]
featureid = json["results"][0]["attrs"]["featureId"]

print(f"{detail} \n {featureid}")

pprint(json)

# %% [markdown]
# ## Height from coordinates
# 
# [docs height](https://api3.geo.admin.ch/rest/services/height)
# 
# 

# %%



url = "https://api3.geo.admin.ch/rest/services/height"
params = {
    "easting": 2600000,
    "northing": 1200000
          }
response = requests.get(url, params)
json = response.json()
print(json)

# %% [markdown]
# ## gebaeude_wohnungs_register
# 
# 

# %%

url = f"https://api3.geo.admin.ch/rest/services/ech/MapServer/ch.bfs.gebaeude_wohnungs_register/{featureid}"

response = requests.get(url)
json = response.json()


atr = json["feature"]["attributes"]

dkode = atr["dkode"]
dkodn = atr["dkodn"] 

print(f"{dkode =        }")
print(f"{dkodn =        }")
pprint(json)



# %% [markdown]
# ## Solardach energie
# 
# solarenergie-eignung-daecher

# %%
## Solardach energie

cordiantes = str(dkode) + "," + str(dkodn)

print(cordiantes)
link = "https://api3.geo.admin.ch/rest/services/all/MapServer/identify"

query = {
	"geometry": cordiantes,
	"geometryFormat": "geojson",
	"geometryType": "esriGeometryPoint",
	"imageDisplay": "1410,620,96",
	"lang": "de",
	"layers": "all:ch.bfe.solarenergie-eignung-daecher",
	"limit": "10",
	"mapExtent": "2683322.444874717,1250605.7978890815,2683674.944874717,1250760.7978890815",
	"returnGeometry": "true",
	"sr": "2056",
	"tolerance": "10"
}

response = requests.get(link, query)
pv_json = response.json()

print(f'How many: {len(pv_json["results"])}')

pprint(pv_json['results'][0]["properties"])


# %%
from IPython.display import display, HTML, IFrame

feature_ids=[]
for i in pv_json["results"]:
	feature_ids.append(i["featureId"])
print(feature_ids)
	





# %%
import matplotlib.pyplot as plt

klasse = pv_json["results"][0]["properties"]['klasse_text']
finanzertrag = pv_json["results"][0]["properties"]["finanzertrag"]
mstrahlung = pv_json["results"][0]["properties"]["mstrahlung"]
neigung = pv_json["results"][0]["properties"]["neigung"]

fig, ax = plt.subplots()
x = pv_json["results"][0]["properties"]["monate"]
y = pv_json["results"][0]["properties"]["monats_ertrag"]
ax.bar(x, y, )
ax.set_ylabel('fruit supply')
ax.set_title('Fruit supply by kind and color')

print(f"{finanzertrag = }")
print(f"{mstrahlung = }")
print(f"{neigung = }")
print(f"{klasse = }")

plt.show()


# %% [markdown]
# ## Heizgradtage
# 
# > Heizgradtage werden verwendet, um den jährlichen Heizwärmebedarf auf die Kalendermonate zu verteilen. Die Heizgradtage für einen Monat berechnen sich aus der Differenz zwischen der Raumtemperatur (20°C) und der Tagesmitteltemperatur an Tagen mit einer Tagesmitteltemperatur tiefer als die Heizgrenze (< 12°C).
# 
# 

# %%

fig, ax = plt.subplots()

x = pv_json["results"][0]["properties"]["monate"]
y = pv_json["results"][0]["properties"]["heizgradtage"]
ax.bar(x, y, color="red")

ax.set_ylabel('Hours')
ax.set_xlabel('Months')
ax.set_title('heizgradtage')


plt.show()
print(y)



