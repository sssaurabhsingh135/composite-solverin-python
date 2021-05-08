import numpy as np
matrix = []
input('Q')
for i in range(3):
   
  row = list(map(float, input().split()))
  matrix.append(row)

inv = np.linalg.inv(matrix)
s11 = inv[0,0]
s12 = inv[0,1]
s22= inv[1,1]
s66 = inv[2,2]

G12 = 1/s66
E2 = 1/s22
E1 = 1/s11
v12 = s12/s11 * -1

with open ("Q_to_Intial.text.text","w") as f:
    f.write(f"E1   {E1}\nE2    {E2}\nG12    {G12}\nv12    {v12}")
