#!/bin/bash
awk -v FS="\t" -v OFS="\t" '{print $1,$4,$14,$15}' $1  > $2
