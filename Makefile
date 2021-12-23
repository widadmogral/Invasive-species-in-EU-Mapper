SHELL := /bin/bash
install: populate_database basic
		@echo "Launching webpage"
		flask run
populate_database:
					@echo "Populating database"
					python3 load_to_sqlite.py
					@cleaning up unecessary files
					@rm -rf dataset/
					@rm multimedia.txt citations.txt verbatim.txt rights.txt metadata.xml meta.xml
download_and_install: downloadgbif populate_database basic download_and_transform
					@echo "Launching webpage"
					flask run

downloadgbif: downloadEASIN downloadjq
			echo "User input required for gbif data Download. Make sure you have a login and password for gbif.org"
			@chmod +x userinput.sh
			source userinput.sh
			@chmod +x gbif_apicall.sh
			./gbif_apicall.sh > gbifcurlresponse.txt
			wget https://api.gbif.org/v1/occurrence/download/request/$$(tail -n1 gbifcurlresponse.txt).zip
			python3 gbif_populate_taxonkeys.py

downloadEASIN:
			python3 EASIN_apicalls.py
basic:
		pip install -r requirements.txt
downloadjq:
		wget -O jq https://github.com/stedolan/jq/releases/download/jq-1.5/jq-linux64
		chmod +x ./jq
download_and_transform:
		@echo "Downloading data from wikipedia"
		@echo "This will take a while"
		python3 wikipedia_extract.py
		@echo "Transforming Data"
		./createimagetsv.sh multimedia.tsv media.tsv
		./createtsv.sh occurrence.txt loadtodb.tsv


