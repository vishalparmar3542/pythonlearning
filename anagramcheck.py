str1="stht"
str2="ssth"
count=1
def fun(str1):
    dict={}
    for i in str1:
        if i in dict:
            dict[i] =  dict.get(i)+1
        else:
            dict[i]=1
    return dict
d=fun(str1)
for i in str2:
    if i in d:
        d[i] =  d.get(i)-1
    else:
        print("not anagram")
        count=0 
        break
  
for i in d.values():
    if(i!=0):
        print("not anagram") 
        count=0  
        break
if count==1:
     print("yes anagram") 