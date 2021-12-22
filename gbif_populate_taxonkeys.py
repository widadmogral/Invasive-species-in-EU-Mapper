import json
import requests

def modify_json_query():
    f = open('query.json','r')
    gbiftaxon_key_file = open('taxon_id_list.txt')
    j = json.load(f)
    f.close()
    if j['predicate']['predicates'][5]['values']:
       print('Taxon key field not empty in query.json')
    else:
       lines = gbiftaxon_key_file.readlines()
       lines = [line.rstrip() for line in lines]
       for line in lines:
           j['predicate']['predicates'][5]['values'].append(int(line))
       f = open('query.json', 'w')
       json.dump(j,f,indent=4)
       f.close()
       print('query.json populated with invasive species ids')
    gbiftaxon_key_file.close()
    f.close()
def get_gbif_taxonkeys():
    species_list_file = open('invasive_species_eu.txt', 'r')
    gbiftaxon_key_file = open('taxon_id_list.txt', 'w')
    url = 'https://api.gbif.org/v1/species/match?name='
    species_name_list = species_list_file.readlines()
    for name in species_name_list:
        species_url=url+name
        species_url=species_url.replace(" ","%20")
        r = requests.get(species_url)
        content = r.json()
        try:
            print(content['usageKey'],file =gbiftaxon_key_file)
        except:
            print(content['usageKey'])
    species_list_file.close()
    gbiftaxon_key_file.close()
def main():
    get_gbif_taxonkeys()
    modify_json_query()
if __name__ == "__main__":
    main()






