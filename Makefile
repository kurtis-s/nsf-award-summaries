data/grants.csv: data/grants.html
	python data/parsedata.py	

data/grants.html: data/getdata.py
	python data/getdata.py $(dir $@)
