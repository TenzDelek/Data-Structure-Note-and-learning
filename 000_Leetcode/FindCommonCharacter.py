#https://leetcode.com/problems/find-common-characters/description/?envType=daily-question&envId=2024-06-05
'''
reflection: -- not able to come up by myself used neetcode
we have to use hashmap.
the logic is simple but hard to code.
suppose we have ["label","bella","roller"]
- think that we dont have to check for each word right..
    only the first word is enough. because if it is not in the first word 
    then it will surely not be in the rest.
- so first we take the frequency(python we have counter).
now we traverse through the array above
and for each word we make a counter(hashmap)
and in the nested loop we go through each char of the first hashmap that we created.
and replace the value by it min. because suppose we have [1,1,2] we have to take 1 because
1 is common to all three.

so after that iteration we will get the same as if it is not 0 it means it is common to all
so use again  a loop and store the label where val is not 0
'''
from collections import Counter
class Delek:
    def commonchar(self,arr:list[str]):
        hashi=Counter(arr[0])
        print(f'count: {hashi}')
        for i in arr:
            curhashi=Counter(i)
            for w in hashi:
                hashi[w]=min(hashi[w],curhashi[w])
        #we get common
        res=[]
        for i,val in hashi.items():
            if val!=0:
                for ins in range(val):
                    res.append(i)
        print("answer:")
        print(res)
if __name__=="__main__":
    obj=Delek()
    strarr=["cool","lock","cook"]
    obj.commonchar(strarr)