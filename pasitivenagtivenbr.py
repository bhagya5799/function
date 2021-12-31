def list(x):
	p=[]
	n=[]
	i=0
	while i<len(x):
		if x[i]<0:
			n.append(x[i])
		if x[i]>0:
			p.append(x[i])
		i+=1
	print('negaitive:',n)
	print('positive nbr:',p)
a=[2,-7,5,-64,-14]
list(a)