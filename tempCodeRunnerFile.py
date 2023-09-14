import numpy as np
arr=np.array([[12,12,12,12,0,0,19,15,15,0],[0,12,12,9,0,13,14,7,15,0],[12,8,0,12,0,13,0,0,15,0]])
for i in range(0,3):
    k=0
    for j in range(0,10):
        if(arr[i][j]!=0):
            k+=1
        else:
            while( k<=9  and arr[i][k]==0):
                k+=1
            if(k<=9):
                temp=arr[i][k]
                arr[i][k]=arr[i][j]
                arr[i][j]=temp
                k+=1
print(arr)