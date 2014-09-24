import argparse
import requests
import os

#Specify the file output path
parser = argparse.ArgumentParser()
parser.add_argument('outpath', help="path to output directory")
args = parser.parse_args()

s = requests.Session()

#We have to get these other sites first, otherwise nsf.gov
#explodes with code 500 (cookie confusion?)
s.get('http://dellweb.bfa.nsf.gov/Top50Inst2/default.asp')
s.get('http://dellweb.bfa.nsf.gov/Top50Inst2/buttons.asp')
s.get('http://dellweb.bfa.nsf.gov/Top50Inst2/bottom.asp')
s.get('http://dellweb.bfa.nsf.gov/Top50Inst2/options.asp')
s.get('http://dellweb.bfa.nsf.gov/Top50Inst2/TopInst.asp')
params= {
        'Continue': 'View Report',
        'DrillDirInfo': 'NSF',
        'FDrillDirInfo': 'NSF',
        'FY_LOW': '2013',
        'MAXROWS': '150',
        'PERTYPE': 'All'
        }
s.post('http://dellweb.bfa.nsf.gov/Top50Inst2/bottom.asp', data=params)

r = s.get('http://dellweb.bfa.nsf.gov/Top50Inst2/TopInst.asp')
with open(os.path.join(args.outpath, 'grants.html'), 'w') as fp:
    fp.write(r.text)
