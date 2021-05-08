import numpy as np
import math as mt
import pandas as pd
from fpdf import FPDF
sigma_x = input("Applied sigma_x ")
sigma_y = input("Applied sigma_y ")
gamma_xy= input("Applied Tau_xy ")
E1 = float(input("E1 "))*pow(10,9)
E2 = float(input("E2 "))*pow(10,9)
v12 = float(input("v12 "))
G12 = float(input("G12 "))*pow(10,9)
theta = float(input('Angle '))
#pdf = FPDF()
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
if sigma_x == "" and sigma_y =="" and gamma_xy=="":

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
 

 print(f's11 = {s11}, s12 = {s12}, s22 = {s22}, s66 = {s66} \t Where units in(1/Pa)', '\n\n')
 print('Matrix Q is : \n',Q,'\n', 'Matrix S is \n', np.linalg.inv(Q), '\n')
 print('Matrix Q_bar is  \n', Q_bar,'\n')
 print('Martix S_bar is \n' , np.linalg.inv(Q_bar))

 with open("Solutions.txt ", 'w') as f:
    f.write(f's11 = {s11}, s12 = {s12}, s22 = {s22}, s66 = {s66} ' )
    f.write(f'\n\n Matrix Q is (in Pa) : \n')
    f.write(f'{Q}')
    f.write('\n Matrix S is (in 1/Pa)\n')
    f.write( f'{np.linalg.inv(Q)} \n')
    f.write('Matrix Q_bar is  (in Pa) \n')
    f.write( f'{Q_bar}')
    f.write('\n Martix S_bar is  (in 1/Pa) \n') 
    f.write( f'{np.linalg.inv(Q_bar)} ' )

else:
 sigmax = float(sigma_x)*pow(10,6)
 sigmay = float(sigma_y)*pow(10,6)
 gammaxy = float(gamma_xy)*pow(10,6)
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
 Matrix_Stress = np.array([[sigmax,sigmay,gammaxy]]).reshape(3,1)
 Matrix = np.dot(np.linalg.inv(Q_bar),Matrix_Stress)
 Gs_index = ['e(x)','e(y)','Y(xy)'] 
 Ls_index=['e(1)','e(2)','Y(12)'] 
 Stress_index = ['sigma(1)','sigma(2)','tau(12)'] 
 G_st = pd.Series(Matrix.tolist(),Gs_index)
 local_strains = np.dot(T2,Matrix).tolist()
 local_stress = np.dot(T1,Matrix_Stress).tolist()
 Loc_strain = pd.Series(local_strains,Ls_index)
 Loc_stress = pd.Series(local_stress,Stress_index) 
 print(f's11 = {s11}, s12 = {s12}, s22 = {s22}, s66 = {s66} \t Where units in(1/Pa)', '\n\n')
 print('Matrix Q is : \n',Q,'\n', 'Matrix S is \n', np.linalg.inv(Q), '\n')
 print('Matrix Q_bar is  \n', Q_bar,'\n')
 print('Martix S_bar is \n' , np.linalg.inv(Q_bar),'\n')
 print('The Global Strains matrix\n', G_st,'\n')
 print('The Local Strains\n',Loc_strain,'\n')
 print('The Local Stress in(Pa)\n',Loc_stress,'\n')

 with open("Solutions.txt ", 'w') as f:
    f.write(f's11 = {s11}, s12 = {s12}, s22 = {s22}, s66 = {s66} ' )
    f.write(f'\n\n Matrix Q is (in Pa) : \n')
    f.write(f'{Q}')
    f.write('\n Matrix S is (in 1/Pa)\n')
    f.write( f'{np.linalg.inv(Q)} \n')
    f.write('Matrix Q_bar is  (in Pa) \n')
    f.write( f'{Q_bar}')
    f.write('\n Martix S_bar is  (in 1/Pa) \n') 
    f.write( f'{np.linalg.inv(Q_bar)} \n' )
    f.write('The Global Strains matrix\n')
    f.write(f'{G_st}\n')
    f.write(f'The Local Strains\n {Loc_strain}\n')
    f.write(f'The Local Stress in(Pa)\n{Loc_stress}\n')
 #pdf.add_page()
 #pdf.set_font("Arial", size = 15)
 #pdf.cell(400, 20, txt = f's11 = {s11}, s12 = {s12}, s22 = {s22}, s66 = {s66} ',  
  #     ln = 1, align = 'C') 
 #pdf.cell(400, 20, txt = f'\n\n Matrix Q is (in Pa) : \n', 
  #       ln = 3, align = 'C') 
 #pdf.cell(400, 20, txt = f'{Q}',  
 """/*        ln = 5, align = 'C')
 pdf.cell(400, 20, txt = '\n Matrix S is (in 1/Pa)\n',  
         ln = 7, align = 'C')   
 pdf.cell(400, 20, txt = 'Matrix Q_bar is  (in Pa) \n',  
         ln = 9, align = 'C')
 pdf.cell(400, 20, txt = f'{Q_bar}',  
         ln = 11, align = 'C') 
 pdf.cell(400, 20, txt = '\n Martix S_bar is  (in 1/Pa) \n',  
         ln = 13, align = 'C')
 pdf.cell(400, 20, txt = f'{np.linalg.inv(Q_bar)} \n',  
         ln = 15, align = 'C')         
 pdf.cell(400, 20, txt = 'The Global Strains matrix\n',  
         ln = 17, align = 'C')  
 pdf.cell(400, 20, txt = f'{G_st}\n',  
         ln = 19, align = 'C') 
 pdf.cell(400, 20, txt = f'The Local Strains\n {Loc_strain}\n',  
         ln = 21, align = 'C')    
 pdf.cell(400, 20, txt = f'The Local Stress in(Pa)\n{Loc_stress}\n',  
         ln = 23, align = 'C')       
 pdf.output("trial1234.pdf")     """

