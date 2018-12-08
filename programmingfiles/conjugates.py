def f(l):
	if len(l)!=1:
		L=[]
		a1=len(l)
		L+=[a1]
		count=1
		while len(L)<max(l):
			c=1
			for j in range(2,max(l)+1):
				for k in range(1, len(l)):
					if l[k]>=j:
						c+=1
				L+=[c]
				c=1
		return L
	else:
		return l
n=int(input('Enter the number of integers\n'))
l=[]
for i in range(n):
	l+=[int(input("Enter an integer:"))]	
print(f(l))			
						