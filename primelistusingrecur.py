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

def adding(count,n):
    if(count>=30):
        return []
    if checkprime(n):
        lst=adding(count+1,n+1)
        lst.append(n)
    else:
        n+=1
        lst=adding(count,n)
    return lst


lst=adding(0,0)
print(lst)