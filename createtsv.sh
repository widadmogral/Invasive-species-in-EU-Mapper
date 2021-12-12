#!/bin/bash
awk -v FS="\t" -v OFS="\t" '{print $1,$62,$99,$121,$133,$134,$233}' $1  > $2
