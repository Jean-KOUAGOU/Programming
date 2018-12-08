from math import sqrt, floor
def f(n):
	if floor(sqrt(n))==sqrt(n):
		print(n,' is a square\n')
	else:	
		a=''	
		for i in range(0,floor(sqrt(n))+1):
			for j in range(0, floor(sqrt(n))+1):
				if i**2+j**2==n:
					print(i,j)
					a='yes'
					break
		if a=='yes':
			print()
			print(n,': Yes\n\n')
		else:
			print(n,' :No')
			print()				
for n in range(1,999):
	if n%4==3:	
		f(n)	