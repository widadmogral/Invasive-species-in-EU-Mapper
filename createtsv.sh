#!/bin/bash
# cherry pick columns required for our purposes. Split scientific name to include only two words
awk -v FS="\t" -v OFS="\t" 'NR==1{print $1,$62,$99,$121, $133, $134, $220, $233} {split($233,a," "); $233 = a[1]" " a[2]; print $1,$62,$99,$121,$133,$134,$220,$233}' $1 > $2
#awk -v FS="\t" -v OFS="\t" '{print $1,$62,$99,$121,$133,$134,$220,$233}' $1  > $2
