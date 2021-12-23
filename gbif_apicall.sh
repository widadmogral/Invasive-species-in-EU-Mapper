jq '.creator=env.GBIFUSER' query.json >> tmp.json && mv tmp.json query.json
jq '.notificationAddresses[0]=env.GBIF_EMAIL' query.json >> tmp.json && mv tmp.json query.json
curl --include --user $GBIFUSER:$GBIFPWD --header Content-Type:application/json --data @query.json https://api.gbif.org/v1/occurrence/download/request

