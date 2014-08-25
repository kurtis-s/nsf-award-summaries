datadir = data

$(datadir)/grants.csv $(datadir)/grants.json: $(datadir)/grants_geocoded.pkl
	python $(dir $@)/exporter.py $< $(dir $@)

$(datadir)/grants_geocoded.pkl: $(datadir)/grants_not_geocoded.pkl
	python $(dir $@)/getgeocodes.py $< $(dir $@)

$(datadir)/grants_not_geocoded.pkl: $(datadir)/grants.html
	python $(dir $@)/parsedata.py $< $(dir $@)

$(datadir)/grants.html: $(datadir)/getdata.py
	python $(dir $@)/getdata.py $(dir $@)

clean:
	rm -f $(datadir)/grants.html
	rm -f $(datadir)/grants_not_geocoded.pkl
	rm -f $(datadir)/grants_geocoded.pkl
	rm -f $(datadir)/grants.csv
	rm -f $(datadir)/grants.json
