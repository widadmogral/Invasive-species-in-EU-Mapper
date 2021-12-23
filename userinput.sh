#!/bin/bash
set -o allexport                #All variables are auto set to export
echo "Setting up environment variables with username and password for gbif.org. This is stored in your home environment for this session only"
echo "Enter user email for Gbif.org:"
read input
GBIFEMAIL=$input
echo "Enter user name for Gbif.org:"
read input
GBIFUSER=$input
echo "Enter password for Gbif.org:"
read input
GBIFPWD=$input
./jq '.creator=env.GBIFUSER' query.json >> tmp.json && mv tmp.json query.json
./jq '.notificationAddresses[0]=env.GBIF_EMAIL' query.json >> tmp.json && mv tmp.json query.json
curl --include --user $GBIFUSER:$GBIFPWD --header Content-Type:application/json --data @query.json https://api.gbif.org/v1/occurrence/download/request