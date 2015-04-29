#Input: 
#Output:
#len(text) < L: iterate till len(text) - curr_pos else: iterate till L
#Usage: python pattern_clump.py 
import sys,re

if len(sys.argv) == 1:
	text = "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"
	k = 5	#kmer
	L = 75	#maximum genome interval within which the kmer must be present multiple times with atleast a frequency of t
	t = 4 	# frequency
else:
	f = open(sys.argv[1])
	text = f.readline().strip()
	k,L,t = f.readline().strip().split()
	k,L,t = int(k),int(L),int(t)

d = {}
for i in range( len(text) - k + 1 ):
	temp = {}
	if i < ( len(text) - L ):
		window = L
	else:
		window = len(text) - i 
	for j in range( i,(i+window) ):
		key = text[j:j+k]
		temp[key] = temp.get(key,0) + 1
	for i,v in temp.items():
		if v >= t:
			d[i] = v
for i in d:
	print i,



