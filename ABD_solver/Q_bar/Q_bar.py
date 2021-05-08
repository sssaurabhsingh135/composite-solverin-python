import numpy as np
import math as mt

E1 = float(input("E1 "))
E2 = float(input("E2 "))
v12 = float(input("v12 "))
G12 = float(input("G12 "))
theta1 = float(input('Angle 1 '))
theta2 = float(input('Angle 2 '))
theta3 = float(input('Angle 3 '))
theta4 = float(input('Angle 4 '))
#pdf = FPDF() 
def angle (theta):
 agl = (mt.pi /180)*theta
 m = mt.cos(agl)
 n = mt.sin(agl)
 cm = m*m 
 cn = n*n
 cmn = m*n 
 cm_n = cm-cn 
 a = E1 
 c =  -v12  
 d = E2 
 s11 = 1/a  
 s22 = 1/d 
 s12 = c/a
 s66 = 1/G12

 def inverse33(b11,b12,b13,b21,b22,b23,b31,b32,b33):
    matrix_33 = np.array([[b11,b12,b13],[b21,b22,b23],[b31,b32,b33]])
    return np.linalg.inv(matrix_33)
 def inverse3(a11,a12,a21,a22,a33):
    matrix_3 = np.array([[a11,a12,0],[a21,a22,0],[0,0,a33]])
    return np.linalg.inv(matrix_3)

 Q = inverse3(s11,s12,s12,s22,s66) 
 T1_inverse = inverse33(cm,cn,2*cmn,cn,cm, -2*cmn, -cmn, cmn, cm_n) 
 T1= np.linalg.inv(T1_inverse)
 T2_inverse = inverse33(cm,cn,cmn,cn,cm, -cmn, -2*cmn, 2*cmn, cm_n)
 T2= np.linalg.inv(T2_inverse)


 Q_b = np.dot(T1_inverse,Q)
 Q_bar = np.dot(Q_b , T2) 
 return Q_bar

with open ('Q_bar.text','w') as f:
  f.write(f'Q_bar at angle1 {theta1}\n{angle (theta1)}\nQ_bar at angle2 {theta2}\n{angle (theta2)}\nQ_bar at angle3 {theta3}\n{angle (theta3)}\nQ_bar at angle4 {theta4}\n{angle (theta4)}')