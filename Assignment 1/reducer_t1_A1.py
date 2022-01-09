#!/usr/bin/env python3
from operator import itemgetter
import sys

hr=0
hr_count=0
hr_now=0


for i in sys.stdin:
     i=i.strip()
     hr,hrc=i.split('\t', 1)
        
     try:		
          hrc=int(hrc)
        	
     except Exception as e:
          continue
        
     if hr_now==hr:
          hr_count+=hrc
     else:
          if hr_now:
               print('%d\t%d' % (int(hr_now), hr_count))
          hr_now=hr
          hr_count=hrc

if (hr_now == hr):
     print('%d\t%d' % (int(hr_now), hr_count))
