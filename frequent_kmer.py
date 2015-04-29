##Input = text,number
##ACGTTGCATGTCGCATGATGCATGAGAGCT, 4
##output = CATG GCAT
##Usage: python frequent_kmer.py rosalind_1a.txt 
import sys
import operator

if len(sys.argv) == 1:
	text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
	k = 4
	print "This is an example run. Please provide a filename with the text in line #1 and k in line #2"
else:
	fname = sys.argv[1]
	f = open(fname)
	text = f.readline().strip()
	k = int(f.readline().strip())

def freq_kmer(text,k):
	kmer_count = {}
  	for i in range( len(text) - k + 1 ):
		kmer = text[i:i+k]	
		kmer_count[kmer] = kmer_count.get(kmer,0) + 1
		
  	freq = max(kmer_count.items(),key=operator.itemgetter(1))
	max_count = freq[1]
	pattern = [k for k,v in kmer_count.items() if v==max_count]
	return pattern
	
pattern = freq_kmer(text,k)
if len(pattern) == 1:
	print pattern
else:
	for i in pattern:
		print i,
