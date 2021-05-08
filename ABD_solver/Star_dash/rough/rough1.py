import numpy as np
matrix_N=[]
for i in range(3):       # A outer for loop for row entries   
   a =[]   
   for j in range(1):     # A inner for loop for column entries   
      a.append(int(input()))   
   matrix_N.append(a)   

Matrix_Nx = np.asarray(matrix).reshape(3,1)
matrix_M=[]
for i in range(3):       # A outer for loop for row entries   
   a =[]   
   for j in range(1):     # A inner for loop for column entries   
      a.append(int(input()))   
   matrix_M.append(a)  

#Matrix_Mx =  np.asarray(matrix).reshape(3,1)

strain = np.add(np.dot(A_dash,Matrix_Nx),np.dot(B_dash,Matrix_Mx))
kappa = np.add(np.dot(C_dash,Matrix_Nx),np.dot(D_dash,Matrix_Mx))