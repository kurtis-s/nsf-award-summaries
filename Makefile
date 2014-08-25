data/grants.csv: data/grants.html
	python $(dir $@)/parsedata.py $< $(dir $@)

data/grants.html: data/getdata.py
	python $(dir $@)/getdata.py $(dir $@)
