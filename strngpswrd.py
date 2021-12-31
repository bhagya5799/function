print('entr 8chrtr ')
def psw(x,y,z,k):
	if a>'A' and a<'Z':
		if b>'a' and b<'z':
			if c>0 and  c<9:
				if d in ('@','&','$','¢','¥'):
					print(a*2+b*2+str(c)*2+d*2)	
a=input('entr upper case')
b=input('lower case')
c=int(input('entr nbr'))
d=input('entr symbol')
psw(a,b,c,d)