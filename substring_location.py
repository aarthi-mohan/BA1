#Input: GATATATGCATATACTT ATAT
#Output: 1 3 9

import sys

if len(sys.argv) == 1:
	text = "GATATATGCATATACTT"
	substr = "ATAT"
else:
	f = open(sys.argv[1])
	substr = f.readline().strip()
	text = f.readline().strip()
	

k = len(substr)
d = {}

for i in range(len(text) - k +1 ):
	key = text[i:i+k]
	if not key in d:
	    d[key] = []
	    d[key].append(i)
	else:
	    d[key].append(i)

print " ".join(str(x) for x in d[substr])
