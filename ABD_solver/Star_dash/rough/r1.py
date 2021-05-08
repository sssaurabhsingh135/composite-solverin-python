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
  
print(np.dot(matrix,matrix1))