import argparse
import os
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('inputfile', help='path to dataframe to be geocoded')
parser.add_argument('outputdir', help='path to the output directory')
args = parser.parse_args()

grant_data = pd.read_pickle(args.inputfile)
grant_data.to_json(os.path.join(args.outputdir, 'grants.json'))
grant_data.to_csv(os.path.join(args.outputdir, 'grants.csv'))
