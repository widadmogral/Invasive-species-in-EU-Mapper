import requests
def api_call_by_kingdom(kingdom, f):
    pagination_max = 50 #EASIN Api calls return only 50 records at a time
    skip_records = 0
    url = 'https://easin.jrc.ec.europa.eu/api/cat/kingdom/'+kingdom+'/take/' + str(pagination_max) + '/skip/' + str(
        skip_records)
    r = requests.get(url)
    header_length = 1000
    tot_length = 0
    while (header_length >= 1000):
        content = r.json()
        for i in range(0, len(content['results'])):
            print(content['results'][i]['SpeciesName'], file=f)
            print(content['results'][i]['SpeciesName'])
        skip_records += 50
        url = 'https://easin.jrc.ec.europa.eu/api/cat/kingdom/animalia/take/' + str(pagination_max) + '/skip/' + str(
            skip_records)
        r = requests.get(url)
        header_length = int(r.headers['Content-Length'])
        tot_length += len(content['results'])
        print(tot_length)

def main():
    species_list_file = open('invasive_species.txt', 'a')
    kingdoms = ['animalia', 'plantae','fungi']  # only animals, plants and fungi are being considered since these would have photographs uploaded
    tot_length = 0
    for kingdom in kingdoms:
        api_call_by_kingdom(kingdom, species_list_file)
    species_list_file.close()
if __name__ == "__main__":
    main()


'''

print(r.json())
print(r.status_code)
'''
