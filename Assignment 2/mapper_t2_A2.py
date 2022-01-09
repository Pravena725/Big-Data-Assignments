#!/usr/bin/env python3
import sys, json, math, requests
import ast

def nom(p):
    s=0
    for i in range(5):
        s+=p[i]**2
    
    return math.sqrt(s)

def similarity(p,q):
    if p==q:
        return 1

    p=pe[str(p)]
    q=pe[str(q)]
    n=0
    for i in range(5):
        n=n+p[i]*q[i]
    
    return n/(nom(p)*nom(q))

vFilePath,pageEmbed = sys.argv[1] ,sys.argv[2]
pe=json.load(open(pageEmbed))

f=open(vFilePath)
v={}
for line in f.read().strip('\n').split('\n'):
    (key, val) = line. split(",")
    v[int(key)] = float(val)



for line in sys.stdin:

    ipage,outpage=line.strip().split('  ')
    ipage=int(ipage)
    outpage=json.loads(outpage)
    num=len(outpage)
    print("%d\t%f" % (ipage,0.0))
    for i in outpage:
        if i==ipage:
            continue
        #try:
        c= similarity(ipage,i)* v[ipage]/num
        #except:
        #    c= similarity(ipage,i)* 0.15/num
        print("%d\t%f" % (i,c))




