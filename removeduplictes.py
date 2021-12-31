def list(x):
	i=0
	b=[]
	while i<len(x):
		if x[i] not in b:
			b.append(x[i])
			i+=1
			print(b)
a=['jan','kan','van','kan','van','jan']
list(a)