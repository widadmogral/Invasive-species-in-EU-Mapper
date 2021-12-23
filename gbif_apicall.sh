tmp/jq '.creator=env.GBIF_USER' query.json >> tmp.json && mv tmp.json query.json
tmp/jq '.notificationAddresses[0]=env.GBIF_EMAIL' query.json >> tmp.json && mv tmp.json query.json
curl --include --user $GBIF_USER:$GBIF_PWD --header Content-Type:application/json --data @query.json https://api.gbif.org/v1/occurrence/download/request > tmp/gbifcurlresponse.txt

