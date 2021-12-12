#!/bin/bash
awk -v FS="\t" -v OFS="\t" '{print $1,$3,$4,$14}' $1  > $2
