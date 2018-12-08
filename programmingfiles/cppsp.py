import random
def configuration(n):
	L=10
	h_init=L/(2*(n-1))
	c1=random.choice(range(0,int(L/2)))
	C=[c1]
	for i in range(1,n):
		C.append(c1+h_init*i)
	def compute_pE(C):
		p_E=0
		for i in range(len(C)-1):
			p_E+=1/(C[i+1]-C[i])
		return p_E
	p_E1=compute_pE(C)
	def search_best_config(n,p_E1):
		C1=C
		p_E2=p_E1
		
		for i in range(n):
			delta_x=(2*random.random()-1)*0.1*(L/(n-1))
			memory=C1[i]
			C1[i]+=delta_x
			if C1[i]<0:
				C1[i]=0
			if C1[i]>L:
				C1[i]=L
			p_E3=compute_pE(C1)
			if p_E3<p_E2:
				p_E2=p_E3
			else:
				C1[i]=memory
		T=[C1,p_E2]
		print(T[0])	
		return T[1]
	eps=0.0
	for i in range(1000):
		search_best_config(n,p_E1)
		p_E1=search_best_config(n,p_E1)
		 	
print(configuration(5))