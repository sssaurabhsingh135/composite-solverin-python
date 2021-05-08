import numpy as np
import math as mt
theta = float(input('Angle '))
#pdf = FPDF()
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
with open("T1_T2_6x6.txt",'w') as f:
   f.write(f'Ti is \n {T1}\n T2 is \n{T2}')

print(f'Ti is \n {T1}\n',f'T2 is \n{T2}')