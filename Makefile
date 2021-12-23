install: populate_database
		@echo "Installing requirements"
		@pip install -r requirements.txt
		@echo "Launching webpage"
		flask run
populate_database:
					@echo "Populating database"
					python3 load_to_sqlite.py






