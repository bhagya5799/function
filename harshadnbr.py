def nbr(x):
	sum=0
	temp=x
	while temp>0:
		r=temp%10
		sum=sum+r
		temp=temp//10
	if x%sum==0:
		print('harshad nbr')
	else:
		print('not harda nbr')
a=int(input('entr nbr'))
nbr(a)