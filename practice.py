import numpy as np
arr = np.empty((8,8),dtype=int)
for i in range(0,8):
    for j in range(0,8):
        if(i%2==0):
            if(j%2==0):
                arr[i][j]=0
            else:
                arr[i][j]=1
        else:
            if(j%2==0):
                arr[i][j]=1
            else:
                arr[i][j]=0
print(arr) 
