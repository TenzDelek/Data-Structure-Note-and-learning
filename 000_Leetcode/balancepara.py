class Delek:
    def paracheck(self,s:str)->bool:
        stack1=[]
        for i in s:
            if i=="(" or i=="[" or i=="{":
                stack1.append(i)
            elif stack1 and i==")" and stack1[-1]=="(":
                stack1.pop()
            elif stack1 and i=="]" and stack1[-1]=="[":
                stack1.pop()
            elif stack1 and i=="}" and stack1[-1]=="{":
                stack1.pop()
            else:#if and closing at last but has no pair
                return False
        return not stack1

if __name__=="__main__":
    obj=Delek()
    res=obj.paracheck("[]")
    print(f"the answer of this question is {res}")

# this question checks your stack skill another way is you can use 
# hash where you store the two key and pair