# Invasive Species in EU Mapper
A web app using the power of citizen data. This app lets an user find out information out Invasive species of EU concern that has been reported anywhere in the EU from various sources. 

 
Table of Contents
=================

 * [Why?](#why)
 * [Main data sources](#Main-data-sources)
 * [Feature implementation status](#Feature-implementation-status)
 * [Installation](#Installation-and-running)
 * [Usage](#Usage)
 * [Git Integration](#Git-integration)

### Why?

I wanted to create a website that:

+ Harnesses the power of citizen data
+ A Layperson could search for invasive species in a given location on a map
+ The website should also work as a look up tool to cross reference a sighting a person had with a previously reported sighting
+ Give some information about sightings- pictures, wikipedia links to more info etc.

### Main data sources

+ EASIN European Alien Species Information Network [API](https://easin.jrc.ec.europa.eu/api/cat/euconcern).
 I am using only species that are marked as of EU CONCERN. As of now 48 species in all.
+ GBIF—the Global Biodiversity Information Facility—is an international network and data infrastructure funded by the world's governments and aimed at providing anyone, anywhere, open access to data about all types of life on Earth. This gives us access to data uploaded by users of many websites and mobile applications from across users that have uploaded their sightings on these platforms. 


### Installation and running
---

Select one of the following methods:

#### Method 1:

In this method you use the data from this repository. It is updated every month.
On the command line Type:
```git clone https://github.com/widadmogral/Invasive-species-in-EU-Mapper
cd Invasive-species-in-EU-Mapper/
 make install```
This will also take care of installing additional dependencies. If you dont want the dependencies to persisit. consider running this in a virtual environment.

This will run the flask web application that will run at http://127.0.0.1:5000 You can open this in your web browser.


#### Method 2:

In this method you create your own dataset and dowload it from gbif.org. The second option will require you to create a username and login. You can also custimize countries you would like to see viewings for by editing the query.json file.


``` make download_and_install```

### Usage
---




#### Git integration





