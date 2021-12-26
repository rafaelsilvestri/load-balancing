#!/bin/bash

BASE_URL="http://localhost:8080"

while true; do
	RESULT=$(curl -s -X GET "$BASE_URL")
	echo "$RESULT - $(date -u)"
	sleep 1
	
done
