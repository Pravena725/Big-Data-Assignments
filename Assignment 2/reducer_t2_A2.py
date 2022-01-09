#!/usr/bin/env python3
import sys, json, math, requests

curPage=None
rank=0


for line in sys.stdin:
    line=line.strip().split('\t')
    cp=int(line[0])
    con=float(line[1])

    if curPage==cp:
        rank+=con

    else:
        if curPage!=None:
            rank=rank*0.85+0.15
            print(curPage,',',"{:0.2f}".format(rank),sep='')
        curPage=cp
        rank=con

if curPage!=None:
    rank=rank*0.85+0.15
    print(curPage,',',round(rank,2),sep='')