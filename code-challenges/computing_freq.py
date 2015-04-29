def pattern2number(text):
	code = {"A":0,"C":1,"G":2,"T":3}	
	sum = 0
	for i in range(len(text)):
		sum += code[text[i]] * ( 4 ** (len(text)-1-i))   
	return sum


def number2pattern(number):
	code = {"A":0,"C":1,"G":2,"T":3}
	rev = {0:"A",1:"C",2:"G",3:"T"}
	reml = []
	quo = 0
	while quo  != 1:
		#print number, 
		quo = number/4
		rem = number%4
		reml.append(rem)
		number = quo
		#print quo,rem
	reml.append(quo)
	return "".join(rev[i] for i in reml)

d = []
text = "ACGCGGCTCTGAAA"
k = 2
for i in range(0, (4**2)):
	d.append(0)
pattern = []
pattern_number = []
for i in range(len(text) - k + 1):
	number = pattern2number(text[i:i+k])
	d[number] += 1
	pattern.append(text[i:i+k])
	pattern_number.append(number)
for i in d:
	print i,