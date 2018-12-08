#def test(n):
def f(n):
	c=0
	p=0
	for d in range(1,n+1):
		if n%d==0:
			c+=1
			p+=d
	return (n,c,p)
print('n, Sigma and Tho:')
#for n in range(2,220):
#	print(f(n))
print(f(85085))