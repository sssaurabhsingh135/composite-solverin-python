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

Matrix_A = np.asarray(matrix)
Matrix_B=np.asarray(matrix1)
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

print(Matrix_D)




with open('Star_matrix.txt','w') as f:
    f.write(f'A_star\n{A_star}\nB_star\n{B_star}\nC_star\n{C_star}\nD_star\n{D_star}\nA_dash\n{A_dash}\nB_dash\n{B_dash}\nC_dash{C_dash}\nD_dash{D_dash}')
