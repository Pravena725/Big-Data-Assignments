#!/usr/bin/env python3
import datetime
import json
import sys
import math

for line in sys.stdin:
	try:
		data = json.loads(line.strip())
		if "lane blocked" in data["Description"].lower() or "shoulder blocked" in data["Description"].lower() or "overturned vehicle" in data["Description"].lower():
			if(data["Severity"]>=2):
				if("Night"==data["Sunrise_Sunset"].strip()):
					if(data["Visibility(mi)"]<=10.0):
						if(data["Precipitation(in)"]>=0.2):
							if (("Heavy Rain"==data["Weather_Condition"].strip()) or ("Heavy Snow"==data["Weather_Condition"].strip()) or ("Thunderstorm"==data["Weather_Condition"].strip()) or ("Heavy Rain Showers"==data["Weather_Condition"].strip()) or ("Blowing Dust"==data["Weather_Condition"].strip())):
								print('%d\t%d' % (int(data["Start_Time"][11:13]),1))
                                
	except Exception as e:
		continue
