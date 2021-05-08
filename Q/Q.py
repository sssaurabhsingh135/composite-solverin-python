import numpy as np
import math as mt
E1 = float(input("E1 "))
E2 = float(input("E2 "))
v12 = float(input("v12 "))
G12 = float(input("G12 "))

#pdf = FPDF()
# agl = (mt.pi /180)*theta
# m = mt.cos(agl)
# n = mt.sin(agl)
# cm = m*m 
# cn = n*n
# cmn = m*n 
# cm_n = cm-cn 
a = E1 
c =  -v12  
d = E2 
s11 = 1/a  
s22 = 1/d 
s12 = c/a
s66 = 1/G12

def inverse3(a11,a12,a21,a22,a33):
    matrix_3 = np.array([[a11,a12,0],[a21,a22,0],[0,0,a33]])
    return np.linalg.inv(matrix_3)

Q = inverse3(s11,s12,s12,s22,s66) 
with open ('Q.txt','w') as f:
    f.write(f'matrix Q GPa\n{Q}')