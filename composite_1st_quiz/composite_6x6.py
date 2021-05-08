import numpy as np
import math as mt


E1 = float(input("E1 "))
E2 = float(input("E2 "))
E3 = float(input("E3 "))
v12 = float(input("v12 "))
v23 = float(input("v23 "))
G12 = float(input("G12 "))
G23 = float(input("G23 "))
theta = float(input('Angle '))
S11 = 1/E1
S12 = -v12/E1
S13 = S12
S21 = S12
S22 = 1/E2
S23 = -v23/E3
S31 = S13
S32 = S23
S33 = S22
S44 = 1/G23
S55 = 1/G12
S66= S55
agl = (mt.pi /180)*theta
m = mt.cos(agl)
n = mt.sin(agl)
cm = m*m 
cn = n*n
cmn = m*n 
cm_n = cm-cn 
def inverse66(b11,b12,b13,b14,b15,b16,b21,b22,b23,b24,b25,b26,b31,b32,b33,b34,b35,b36,b41,b42,b43,b44,b45,b46,b51,b52,b53,b54,b55,b56,b61,b62,b63,b64,b65,b66):
    matrix_33 = np.array([[b11,b12,b13,b14,b15,b16],[b21,b22,b23,b24,b25,b26],[b31,b32,b33,b34,b35,b36],[b41,b42,b43,b44,b45,b46]
    ,[b51,b52,b53,b54,b55,b56],[b61,b62,b63,b64,b65,b66]])
    return np.linalg.inv(matrix_33)

T1_inverse = inverse66(cm,cn,0,0,0,2*cmn,cn,cm,0,0,0, -2*cmn,0,0,1,0,0,0,0,0,0,m,-n,0,0,0,0,n,m,0, -cmn, cmn,0,0,0, cm_n) 
T1= np.linalg.inv(T1_inverse)
T2_inverse = inverse66(cm,cn,0,0,0,cmn,cn,cm,0,0,0, -cmn,0,0,1,0,0,0,0,0,0,m,-n,0,0,0,0,n,m,0, -2*cmn, 2*cmn,0,0,0, cm_n)
T2= np.linalg.inv(T2_inverse)
MAT_S=np.linalg.inv(inverse66(S11,S12,S13,0,0,0,S21,S22,S23,0,0,0,S31,S32,S33,0,0,0,0,0,0,S44,0,0,0,0,0,0,S55,0,0,0,0,0,0,S66))
MAT_C= inverse66(S11,S12,S13,0,0,0,S21,S22,S23,0,0,0,S31,S32,S33,0,0,0,0,0,0,S44,0,0,0,0,0,0,S55,0,0,0,0,0,0,S66)
Q_b = np.dot(T1_inverse,MAT_C)
C_bar = np.dot(Q_b , T2) 
S_bar=np.linalg.inv(C_bar)
print(np.linalg.inv(MAT_C))
print(f'The Matrix S (1/GPa) \n{MAT_S}\nThe Matrix C (GPa) \n{MAT_C}\nThe Matrix C_bar (GPa)\n{C_bar}\nThe Matrix S_bar (1/GPa) \n{S_bar} ')
with open("composite_6x6.txt",'w') as f:
   f.write(f'The Matrix S (1/GPa) \n{MAT_S}\nThe Matrix C (GPa) \n{MAT_C}\nThe Matrix C_bar (GPa) \n{C_bar}\nThe Matrix S_bar (1/GPa) \n{S_bar} ')