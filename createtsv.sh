#!/bin/bash
# add header to tsv file
head -n1 $1 > $2 
#add rest of rows
awk -v FS="\t" -v OFS="\t" '{print $1,$62,$99,$121,$133,$134,$220,$233}' $1  > $2
