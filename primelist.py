def checkprime(n):
    if n==2 or n==3:
        return True
    if n%2==0:
        return False
    if n<2:
        return False
    for num in range(3,(int)(n/2)):   
        if n%num==0:
            return False   
    return True

lst=[]
n=1
while(1):
    if checkprime(n):
        lst.append(n)
    if(len(lst)>=30):
        break
    else:
        n+=1
lst.reverse()

# i=0
# j=len(lst)-1
# while(i<len(lst)/2):
#     temp=lst[i]
#     lst[i]=lst[j]
#     lst[j]=temp
#     i+=1
#     j=j-1

print(lst)    

