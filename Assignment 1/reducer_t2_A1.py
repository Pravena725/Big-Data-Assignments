#!/usr/bin/env python3
import sys

flag = 1
citycount=0
statescount=0

for line in sys.stdin:
    line = line.strip()

    state, city = line.split(' ',1)

    if (flag == 1):
        statescount = 0
        print(state)
        pstate = state
        citycount = 0
        pcity = city
        flag = 0
        
        
    if (state == pstate and city == pcity):
        citycount += 1
        
        
    elif (state == pstate and city != pcity):
        statescount += citycount
        print(pcity, citycount)
        citycount = 1
        pcity = city
        
        
        
    elif (state != pstate and city != pcity):
        statescount += citycount
        print(pcity, citycount)
        print(pstate, statescount)
        statescount = 0
        pstate = state
        print(pstate)
        pcity = city
        citycount = 1

if (citycount != 0 and statescount != 0):
    statescount += citycount
    print(pcity, citycount)
    print(pstate, statescount)
