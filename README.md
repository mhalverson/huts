This repo tracks and visualizes the New Zealand backcountry huts I have visited.

# Overview

There are three data sources:

* When I finish a tramping trip, I manually track which huts I visited by
  updating my "trips database" (`trips.py`).
* The exhaustive list of DOC huts was procured by downloading from the NZ
  government data portal
  https://catalogue.data.govt.nz/dataset/doc-huts/resource/5a455699-6d85-4847-a9e8-4e3889d340ad
  on 13 April 2019 (`data/DOC_Huts.geojson`).
* If I visit a non-DOC hut, I add it to a separate, manually maintained list
  (`data/non_DOC_Huts.json`).

There are two main ways to render the data:

* checklist (html or plaintext)
* map

Special call-out that the checklist renderer is agnostic to the input -- the
checkboxes are determined solely by the hut list you pass in. If you pass in a
single hut on the North Island, it will think the North Island only has one
hut. If you don't pass in any huts for Fiordland National Park, it will omit
Fiordland National Park entirely.

The map renderer has the same behavior -- the markers are determined solely by
the hut list you pass in. Any regions not represented in the hut list will be
omitted from the LayerControl.

# Setup

* `python3 -m venv env` to create a virtualenv named env that will hold our
  dependencies in a sandbox
* `. env/bin/activate` to activate the virtualenv
* `pip3 install -r requirements.in` to install the requirements into the
  virtualenv. If you're having dependency version issues, you can see what I
  ended up with in `requirements.txt`. But know that I use `requirements.in` to
  track my immediate dependencies

# Use

## Dev

* `PYTHONPATH=. python3 huts/checklist.py` to generate a checklist of huts
   visited (printed to stdout)
* `jupyter notebook hut_map.ipynb` to start a Jupyter Notebook server for
   exploring maps

## Website

Regenerate the checklist and map files for the website with the following commands:

```
CHECKLIST=matt_checklist.html
PYTHONPATH=. python3 huts/checklist.py html > ../website/tramping/$CHECKLIST
PYTHONPATH=. python3 huts/map.py
NORTH_ISLAND_MAP=north_island_matt_map.html
SOUTH_ISLAND_MAP=south_island_matt_map.html
NORTH_ISLAND_DATA=north_island_matt_data.js
SOUTH_ISLAND_DATA=south_island_matt_data.js
./xform_map_for_website.sh rendered_map.north_island.html $NORTH_ISLAND_DATA > ../website/tramping/$NORTH_ISLAND_MAP
cp checklist_data.north_island.js ../website/tramping/$NORTH_ISLAND_DATA
./xform_map_for_website.sh rendered_map.south_island.html $SOUTH_ISLAND_DATA > ../website/tramping/$SOUTH_ISLAND_MAP
cp checklist_data.south_island.js ../website/tramping/$SOUTH_ISLAND_DATA
```

Update the dynamic build-your-own map data with the following commands:

```
PYTHONPATH=. python3 huts/dynamic_user_map.py
mv encoded_hut_dict.js ../website/tramping/encoded_hut_dict.js
```
