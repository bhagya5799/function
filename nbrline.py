def nbr(x):
	c1 = 0
	while c1 < len(x):
	   small1= len(x[c1])
	   c2 = 0
	   while c2 < small1:
	       print (x[c1][c2])
	       c2 = c2 + 1
	   c1 = c1 + 1
	   print ('-----')
a= [[1,2,3], [5,8,9], [4,3,77,521,31,311]]
nbr(a)