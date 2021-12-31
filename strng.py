def str(a):
	temp=a
	sum=0
	while 0<a:
		fact=1
		i=1
		rem=a%10
		while i<=rem:
			fact=fact*i
			i=i+1
		sum=sum+fact
		a=a//10
	if sum==temp:
		print(temp,'strong nbr')
	else:
		print(temp,'not strong')
n=int(input('entr nbr'))
str(n)