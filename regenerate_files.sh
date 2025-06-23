source env/bin/activate

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

