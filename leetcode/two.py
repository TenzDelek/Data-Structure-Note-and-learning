#gcd
from math import gcd
str1 = "ABABAB"
str2 = "ABAB"
if(str1 +str2)!= (str2+str1):
    print("not equal")
    
ans=gcd(len(str1),len(str2))
res=str1[:ans]
print(res)

