#!/bin/bash

docker stack deploy --compose-file docker-compose.yml ss    

read -p "Enter url : " url

printf "chrome ss"
curl -i -X GET -H "Content-type: application/json" http://localhost:5001/ss/chrome?url=$url

printf "\n firefox ss"
curl -i -X GET -H "Content-type: application/json"  http://localhost:5002/ss/firefox?url=$url

printf "\n"

docker stack rm ss
