#Input = text,number
#ACGTTGCATGTCGCATGATGCATGAGAGCT, 4
#output = CATG GCAT

import operator
def freq_kmer(text,k):
	kmer_count = {}
  	for i in range( len(text) - k + 1 ):
	    kmer = text[i:i+k]
	    if not kmer in kmer_count:
	      kmer_count[kmer] = 1
	    else:
	      kmer_count[kmer] += 1
  #frequent = max(sorted(kmer_count.items(),key=operator.itemgetter(1)))[0]
  #won't work in case of ties
  
	max_count = 0
	for k,v in kmer_count.items():
	if v > max_count:
	  max_count = v
	pattern = [k for k,v in jmer_count.items() if v==max_count]
	return pattern
