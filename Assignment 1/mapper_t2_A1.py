#!/usr/bin/env python3
import sys, json, math, requests
lat = float(sys.argv[1])
lon = float(sys.argv[2])
d = float(sys.argv[3])

# print(lat,lon,d)
def check_nan(parsed):
    attributes = ['Start_Lat','Start_Lng']
    for cond in attributes:
        if str(parsed[cond]) == "nan":
            return 1
for line in sys.stdin:
    line = line.strip()
    parsed = json.loads(line)
    if((check_nan(parsed))):
        continue
    else:
    	start_lat = float(parsed["Start_Lat"])
    	start_lng = float(parsed["Start_Lng"])
    	euc_dist = ((start_lat - lat)**2 + (start_lng-lon)**2)**0.5
    	# print(euc_dist)
    	if(float(d)>=euc_dist):
    		data = {"latitude":start_lat,"longitude":start_lng}
    		response=requests.post('http://20.185.44.219:5000/',json=data)
    		response = json.loads(response.text)
    		print(response['state'],response['city'])
