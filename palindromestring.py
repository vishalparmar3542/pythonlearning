str="abcdcba"
i=0
j=len(str)-1
flag=0
while(True):
    if(i<len(str)/2):
        if(str[i]==str[j]):
            j=j-1
            i=i+1
        else:
            flag=1
            break
    else:
        break
if flag==0:
    print("p")
else:
    print("np")
