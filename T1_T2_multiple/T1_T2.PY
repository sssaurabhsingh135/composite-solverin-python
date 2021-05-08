import numpy as np
import math as mt
theta1 = float(input('Angle 1 '))
theta2 = float(input('Angle 2 '))
theta3 = float(input('Angle 3 '))
theta4 = float(input('Angle 4 '))
#pdf = FPDF()
def Angle(theta):
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
 return f'{T1}\n{T2}' 

with open("T1_T2_3x3.txt",'w') as f:
   f.write(f'T1 and T2 is at {theta1}\n{Angle(theta1)}\nT1 and T2 is at {theta2}\n{Angle(theta2)}\nT1 and T2 is at {theta3}\n{Angle(theta3)}\nT1 and T2 is at {theta4}\n{Angle(theta4)}')

#print(f'Ti is \n {T1}\n',f'T2 is \n{T2}')

with open("Test.txt",'w') as f:
   f.write(f'T1 and T2 is at {theta1}\n{Angle(theta1)}')