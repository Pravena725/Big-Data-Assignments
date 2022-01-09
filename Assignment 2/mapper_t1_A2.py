#!/usr/bin/env python3
import sys, math
d={}
a=[]

for line in sys.stdin:
    line=line.replace('\n','')
    part1,part2=line.split('\t')
    part1=int(part1)
    part2=int(part2)
    print('{},{}'.format(part1,part2))

