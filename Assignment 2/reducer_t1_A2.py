#!/usr/bin/env python3
import sys, math
d={}
a=[]

f=open(sys.argv[1],"w")

for line in sys.stdin:
    line=line.replace('/n','')
    part1,part2=line.split(',')
    part1=int(part1)
    part2=int(part2)
    if part1 not in d:
        d[part1]=[part2]
        f.write(str(part1)+',1\n')
    else:
    	d[part1].append(part2)

f.close()

print('\n'.join("{}   {}".format(k, v) for k, v in sorted(d.items())))

