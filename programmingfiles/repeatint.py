try:
	elemts=[]
	l=[]
	n=int(input('How many integers do you want to enter ?\n\n'))
	print('\nEnter them:\n')
	for i in range(n):	
		l+=[int(input())]
	print('\nThe following numbers are repeated more than one times:\n')
	for i in range(len(l)):
		if not (l[i] in elemts)==True:
			for j in range(len(l)):
				if j!=i and l[j]==l[i]:
					elemts+=[l[i]]
					print(l[i], end=' ')
					break
	print()
except ValueError:
	print('\nEnter a list of integers\n\n')	