import requests
def api_call(f):
    url = 'https://easin.jrc.ec.europa.eu/api/cat/euconcern/' 
    r = requests.get(url)
    content = r.json()
    for i in range(0, len(content['results'])):
        print(content['results'][i]['SpeciesName'], file=f)
def main():
    species_list_file = open('invasive_species_eu.txt', 'w')
    api_call(species_list_file)
    species_list_file.close()
if __name__ == "__main__":
    main()


