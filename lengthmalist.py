def list(x):
 	i=0
 	maxl=0
 	minl=0
 	while i<len(x):
 		if (len(x[i]))>maxl:
 			maxl=len(x[i])
 			min=x[i]
 			print(maxl,min)
 		i+=1

a=[[0],[1, 3], [5, 7], [9, 11], [13, 15, 17]]
list(a)