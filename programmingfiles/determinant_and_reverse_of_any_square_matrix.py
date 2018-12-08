from math import pow
test="n"
n=1
while test=="n" or n<=1:
    n=int(input("Enter the size of the matrix, greater than 1 :\n"))
    A=[[0 for i in range(n)] for j in range(n)]
    print("\nPlease enter the matrix by rows:\n")
    for i in range(n):
        for j in range(n):
            print("\nEnter A[",i,"][",j,"]:\n")
            A[i][j]=float(input())
    print("""The matrix you entered is below, is it what you meant ?\n""")
    for i in range(n):
        print("|",end=" ")
        for j in range(n):
            print(A[i][j],end=" ")
        print("|\n")
    test=input("""\nAnswer by yes "y" or no "n", please: """)
def det(M):
    determinant=0
    n=len(M)
    if n==2:
        return M[0][0]*M[1][1]-M[1][0]*M[0][1]
    else:
        for j in range(n):
            determinant+=pow(-1,j)*M[0][j]*det(select(0,j,M))
        return determinant

def transpose(matrix):
    n=len(matrix)
    C=[[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j]=matrix[j][i]
    return C

def reverse(matrix):
    n=len(matrix)
    Com=[[0 for i in range(n)] for j in range(n)]
    Reverse=Com
    for i in range(n):
        for j in range(n):
            Com[i][j]=pow(-1,i+j)*det(select(i,j,matrix))
    COM=transpose(Com)
    for i in range(n):
        for j in range(n):
            Reverse[i][j]=COM[i][j]
            if Reverse[i][j]==-0.0:
            	Reverse[i][j]=0.0
    return Reverse
def reverse_2(matrix):
    n=len(matrix)
    Com=[[0 for i in range(n)] for j in range(n)]
    Reverse=Com
    Com[0][0]=matrix[1][1]
    Com[0][1]=-matrix[1][0]
    Com[1][0]=-matrix[0][1]
    Com[1][1]=matrix[0][0]
    COM=transpose(Com)
    for i in range(n):
        for j in range(n):
            Reverse[i][j]=COM[i][j]
            if Reverse[i][j]==-0.0:
            	Reverse[i][j]=0.0
    return Reverse
    
def select(t,pos,vide):
    A=vide
    B=[[0 for i in range(len(vide)-1)] for j in range(len(vide)-1)]
    for i in range(len(vide)):
        for j in range(len(vide)):
            if j<pos and i<t:
                B[i][j]=A[i][j]
            elif j<pos and i==t and t<len(vide)-1:
                B[i][j]=A[i+1][j]
            elif j<pos and i==t and t==len(vide)-1:
                B[i-1][j]=A[i-1][j]
            elif j<pos and i>t and i<len(vide)-1:
                B[i][j]=A[i+1][j]
            elif j<pos and i>t and i==len(vide)-1:
                B[i-1][j]=A[i][j]
            elif j==pos and pos<len(vide)-1 and i<t:
                B[i][j]=A[i][j+1]
            elif j==pos and pos<len(vide)-1 and i==t and t<len(vide)-1:
                B[i][j]=A[i+1][j+1]
            elif j==pos and pos<len(vide)-1 and i==t and t==len(vide)-1:
                B[i-1][j]=A[i-1][j+1]
            elif j==pos and pos<len(vide)-1 and i>t and i<len(vide)-1:
                B[i][j]=A[i+1][j+1]
            elif j==pos and pos<len(vide)-1 and i>t and i==len(vide)-1:
                B[i-1][j]=A[i][j+1]
            elif j==pos and pos==len(vide)-1 and i<t:
                B[i][j-1]=A[i][j-1]
            elif j==pos and pos==len(vide)-1 and i==t and t<len(vide)-1:
                B[i][j-1]=A[i+1][j-1]
            elif j==pos and pos==len(vide)-1 and i==t and t==len(vide)-1:
                B[i-1][j-1]=A[i-1][j-1]
            elif j==pos and pos==len(vide)-1 and i>t and i<len(vide)-1:
                B[i][j-1]=A[i+1][j-1]
            elif j==pos and pos==len(vide)-1 and i>t and i==len(vide)-1:
                B[i-1][j-1]=A[i][j-1]
            elif j>pos and j<len(vide)-1 and i<t:
                B[i][j]=A[i][j+1]
            elif j>pos and j<len(vide)-1 and i==t and t<len(vide)-1:
                B[i][j]=A[i+1][j+1]
            elif j>pos and j<len(vide)-1 and i==t and t==len(vide)-1:
                B[i-1][j]=A[i-1][j+1]
            elif j>pos and j<len(vide)-1 and i>t and i<len(vide)-1:
                B[i][j]=A[i+1][j+1]
            elif j>pos and j<len(vide)-1 and i>t and i==len(vide)-1:
                B[i-1][j]=A[i][j+1]
            elif j>pos and j==len(vide)-1 and i<t:
                B[i][j-1]=A[i][j]
            elif j>pos and j==len(vide)-1 and i==t and t<len(vide)-1:
                B[i][j-1]=A[i+1][j]
            elif j>pos and j==len(vide)-1 and i==t and t==len(vide)-1:
                B[i-1][j-1]=A[i-1][j]
            elif j>pos and j==len(vide)-1 and i>t and i<len(vide)-1:
                B[i][j-1]=A[i+1][j]
            elif j>pos and j==len(vide)-1 and i>t and i==len(vide)-1:
                B[i-1][j-1]=A[i][j]
    return B

print("\nThe determinant of the matrix you entered is: ",det(A))
print("\nDo you want to compute the inverse of the matrix ?\n")

answer=input("""Answer by yes "y" or no "n", please: """)
if answer=="y":
    if det(A)!=0:
        if len(A)!=2:
            C=reverse(A)
            print("\n Divide the matrix below by  ",det(A), " to find the inverse :\n")
            for i in range(len(C)):
                print(C[i])
        elif len(A)==2:
            C=reverse_2(A)
            print("\nDivide the matrix below by",det(A), " to find the inverse :\n")
            for i in range(len(C)):
                print("|",end=" ")
                for j in range(len(C)):
                    print(C[i][j],end=" ")
                print("|\n")
    else:
        print("\nThe matrix you entered is not reversible.\n\n")
        
            
            
            
    
    
    
