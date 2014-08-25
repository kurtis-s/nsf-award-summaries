import argparse
from geopy.geocoders.googlev3 import GoogleV3
import numpy as np
import os
import pandas as pd
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument('inputfile', help='path to dataframe to be geocoded')
parser.add_argument('outputdir', help='path to the output directory')
args = parser.parse_args()

grants = pd.read_pickle(args.inputfile)
grants['latitude'] = np.nan
grants['longitude'] = np.nan

geolocator = GoogleV3()
for institution, series in grants.iterrows():
    state = series['state_or_country']
    location = geolocator.geocode(institution + ',' + state)
    sleep(0.1) #Make sure we don't go over Google API limit
    grants.loc[institution, 'latitude'] = location.latitude
    grants.loc[institution, 'longitude'] = location.longitude

grants.to_pickle(os.path.join(args.outputdir, 'grants_geocoded.pkl'))
