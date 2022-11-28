#! /usr/local/bin/bash

URL='http://localhost:9000/suggest?prefix=a&limit=100'

echo "Request output:"
curl -X GET "${URL}"

printf "\n============\n"
echo "Metrics result:"
curl -w "@curl_format.txt" -o /dev/null -s -X GET "${URL}"  -H "accept: application/json"
