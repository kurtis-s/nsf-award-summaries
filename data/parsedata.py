import argparse
import lxml.html
import os
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument('inputfile', help='path to the html input file (from nsf.gov) to be parsed')
parser.add_argument('outputdir', help='path to the output directory')
args = parser.parse_args()

grant_data = {}

parsed_data = lxml.html.parse(args.inputfile)
grant_data['institution'] = [name.strip() for name in parsed_data.xpath('//table/tbody/tr/td/font/a/text()')]
grant_data['state_or_country'] = [state.strip() for state in parsed_data.xpath('//table/tbody/tr/td[2]/font/text()')]
grant_data['grant_amt_thousands'] = [int(amt.strip().strip('$').replace(',', '')) for amt in parsed_data.xpath('//table/tbody/tr/td[3]/font/text()')]

grant_frame = pd.DataFrame.from_dict(grant_data)

grant_frame.to_pickle(os.path.join(args.outputdir, 'grants_not_geocoded.pkl'))
