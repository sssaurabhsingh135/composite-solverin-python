import numpy as np 
import math as mt

theta = float(input('Insert angle\n'))
input("Ensert Matrix")
matrix = []
for i in range(3):
   
  row = list(map(float, input().split()))
  matrix.append(row)


agl = (mt.pi /180)*theta
m = mt.cos(agl)
n = mt.sin(agl)
cm = m*m 
cn = n*n
cmn = m*n 
cm_n = cm-cn 

def inverse33(b11,b12,b13,b21,b22,b23,b31,b32,b33):
    matrix_33 = np.array([[b11,b12,b13],[b21,b22,b23],[b31,b32,b33]])
    return np.linalg.inv(matrix_33)

T1_inverse = inverse33(cm,cn,2*cmn,cn,cm, -2*cmn, -cmn, cmn, cm_n) 
T1= np.linalg.inv(T1_inverse)
T2_inverse = inverse33(cm,cn,cmn,cn,cm, -cmn, -2*cmn, 2*cmn, cm_n)
T2= np.linalg.inv(T2_inverse) 

Q_ = np.dot(T1,matrix)
Q = np.dot(Q_,T2_inverse)

inv = np.linalg.inv(Q)
s11 = inv[0,0]
s12 = inv[0,1]
s22= inv[1,1]
s66 = inv[2,2]

G12 = 1/s66
E2 = 1/s22
E1 = 1/s11
v12 = s12/s11 * -1

with open ("Qbar_to_Intial.text","w") as f:
    f.write(f"E1   {E1}\nE2    {E2}\nG12    {G12}\nv12    {v12}")