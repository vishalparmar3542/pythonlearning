def isprime(num):
    if num==2 or num==3:
        return True
    if num%2==0 or num<2:
        return False
    for n in range(3,int(num**0.5)+1,2):   
        if num%n==0:
            return False   
    return True

pr=0
lis=[2,3,4,5,6,7,8,9]
for x in lis:
    if isprime(x):
        pr=pr+1
        
print(pr)