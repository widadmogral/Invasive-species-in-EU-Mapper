import wikipedia
import csv
import sys
def main(specieslist):
    url ="https://en.wikipedia.org/wiki/"
    csvfile = open('wiki_info.csv', 'w')
    f = open(specieslist,'r')
    writer = csv.writer(csvfile, delimiter='\001')
    writer.writerow(["verbatimScientificName","wiki_url","summary"])
    names = [line.rstrip() for line in f]
    print(names)
    titles = [wikipedia.search(name,results =1) for name in names]
    print(titles)
    urls =[url + title[0] for title in  titles ]
    print(urls)
    '''
    pages = [wikipedia.page(title = title[0]) for title in titles]
    contents = [page.content for page in pages]
    '''
    for i in range(0,len(names)):
        name= names[i].split()[:2] # get only first two words of scientific name
        name = name[0] + " " + name[1] # convert to string
        print(name)
        csvname = r'{}'.format(name) # using raw format to avoid interpretation of content
        csvurl = urls[i].replace(" ","%20")
        csvurl = r'{}'.format(csvurl)
        #csvcontent = r'{}'.format(contents[i])
        writer.writerow([csvname,csvurl])
    csvfile.close()
    f.close()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        specieslist = sys.argv[1]
    else:
        specieslist = 'invasive_species_eu.txt'
    main(specieslist)
