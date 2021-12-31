def  nbr(y):
	for i in range(2,y+1):
		if i>2:
			for j in range(2,i):
				if i%j==0:
					break
			else:
				print(i,'prime')
	
a=int(input('entr end nbr'))
nbr(a)