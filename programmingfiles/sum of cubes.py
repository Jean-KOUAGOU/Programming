from math import sqrt, floor, pow
def f(n):
	if floor(pow(n,1/3))==pow(n,1/3):
		print(n,' is a perfect cube\n')
	else:	
		a=''	
		for i in range(0,floor(pow(n,1/3))+1):
			for j in range(0, floor(pow(n,1/3))+1):
				for k in range(floor(pow(n,1/3))+1):
					if j**3+k**3==n:
						print('Sum of two cubes with:',j,k)	
					if i**3+j**3+k**3==n:
						print(i,j,k)
						a='yes'
						break
		if a=='yes':
			print()
			print(n,': Yes\n\n')
		else:
			print(n,' :No')
			print()
							
for n in range(1,9999):
	if n%27==22:	
		f(n)	