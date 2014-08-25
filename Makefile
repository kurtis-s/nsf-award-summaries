datadir = data

$(datadir)/grants.csv: $(datadir)/grants.html
	python $(dir $@)/parsedata.py $< $(dir $@)

$(datadir)/grants.html: $(datadir)/getdata.py
	python $(dir $@)/getdata.py $(dir $@)

clean:
	rm -f $(datadir)/grants.csv
	rm -f $(datadir)/grants.html
	rm -f $(datadir)/grants.json
