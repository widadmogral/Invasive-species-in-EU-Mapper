import json
f = open('query.json','r')
t = open('taxon_id_list.txt')
j = json.load(f)
f.close()
if j['predicate']['predicates'][5]['values']:
    print('Taxon key field not empty in query.json')
else:
    lines = t.readlines()
    lines = [line.rstrip() for line in lines]
    for line in lines:
        j['predicate']['predicates'][5]['values'].append(int(line))
    f = open('query.json', 'w')
    json.dump(j,f,indent=4)
    f.close()
    print('query.json populated with invasive species ids')





