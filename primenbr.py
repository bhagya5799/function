def prime(x):
	i=2
	while i<x:
		if x%2==0:
			print('not prime')
			break
		i+=1
	else:
			print('prime nbr')
a=int(input('entr nbr'))
prime(a)