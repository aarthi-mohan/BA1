##Input: AAAACCCGGT
##Output: ACCGGGTTTT

import sys, re

f = open(sys.argv[1])
dna = f.readline().strip()

#dna = "AAAACCCGGT"

def replace(dna_ls, position,replace_string):
	for i in position:
		dna_ls[i] = replace_string
	return dna_ls

a = [m.start() for m in re.finditer("A",dna)]
t = [m.start() for m in re.finditer("T",dna)]
c = [m.start() for m in re.finditer("C",dna)]
g = [m.start() for m in re.finditer("G",dna)]

dna_ls = list(dna)
dna_ls	= replace(dna_ls,a,"T")
dna_ls	= replace(dna_ls,t,"A")
dna_ls	= replace(dna_ls,g,"C")
dna_ls	= replace(dna_ls,c,"G")

print ''.join(dna_ls[::-1])



	
