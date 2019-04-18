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

* checklist

* map

# Setup

* `virtualenv env` to create a virtualenv named env that will hold our
  dependencies in a sandbox

* `. env/bin/activate` to activate the virtualenv

* `pip install -r requirements.in` to install the requirements into the
  virtualenv. If you're having dependency version issues, you can see what I
  ended up with in `requirements.txt`. But know that I use `requirements.in` to
  track my immediate dependencies

# Use

* `python huts/checklist.py` to generate a checklist of huts visited (printed to stdout)
* `jupyter notebook hut_map.ipynb` to start a Jupyter Notebook server for exploring maps
