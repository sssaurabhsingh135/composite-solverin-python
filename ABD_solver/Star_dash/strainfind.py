import numpy as np
matrix = []
input('A')
for i in range(3):
   
  row = list(map(float, input().split()))
  matrix.append(row)

input('B')


matrix1 = []

for i in range(3):
   
  row = list(map(float, input().split()))
  matrix1.append(row)

input('D')

matrix2 = []

for i in range(3):
   
  row = list(map(float, input().split()))
  matrix2.append(row)

input('Enter N Matrix')
matrix_N=[]
for i in range(3):       # A outer for loop for row entries   
   a =[]   
   for j in range(1):     # A inner for loop for column entries   
      a.append(float(input()))   
   matrix_N.append(a)   

Matrix_Nx = np.asarray(matrix_N).reshape(3,1)
input('Enter M Matrix')
matrix_M=[]
for i in range(3):       # A outer for loop for row entries   
   a =[]   
   for j in range(1):     # A inner for loop for column entries   
      a.append(float(input()))   
   matrix_M.append(a)  

Matrix_Mx =  np.asarray(matrix_M).reshape(3,1)

Matrix_A = np.asarray(matrix)
Matrix_B=np.asarray(matrix1)*-1
Matrix_D=np.asarray(matrix2)
A_star = np.linalg.inv(Matrix_A)
B_star = np.dot(A_star,Matrix_B)*(-1)
C_star = np.dot(Matrix_B,A_star)

C_ = np.dot(C_star,Matrix_B)
D_star = np.subtract(Matrix_D , C_)

D_star_inv = np.linalg.inv(D_star)
Mult= np.dot(B_star,D_star_inv)*(-1)
MULT1=np.dot(Mult,C_star)

A_dash = np.add( A_star,MULT1)
B_dash = np.dot(B_star,D_star_inv)
C_dash = -1*np.dot(D_star_inv,C_star)
D_dash = D_star_inv
strain = np.add(np.dot(A_dash,Matrix_Nx),np.dot(B_dash,Matrix_Mx))
kappa = np.add(np.dot(C_dash,Matrix_Nx),np.dot(D_dash,Matrix_Mx))
with open('strainfind.txt','w') as f:
    f.write(f'A_star\n{A_star}\nB_star\n{B_star}\nC_star\n{C_star}\nD_star\n{D_star}\nA_dash\n{A_dash}\nB_dash\n{B_dash}\nC_dash{C_dash}\nD_dash\n{D_dash}\nStrain  (*10^-3)\n{strain}\nkappa (1/meter)\n{kappa}')
