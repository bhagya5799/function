def nbr(n):
	if n==1:
		return 1
	else:
		return n*nbr(n-1)
print(nbr(3))