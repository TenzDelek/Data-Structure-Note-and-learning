# l1=[2,4,3]
# l2=[5,6,4]
# strappend=""
# def myfunc(i,l1,strappend):
#     if(i==len(l1)):
#         print("".join(reversed(strappend)))
#         return
#     strappend+=str(l1[i])
#     myfunc(i+1,l1,strappend)

# myfunc(0,l1,strappend)

def recursion(i,n,subset,arr):
    if(i==n):
        res.add(tuple(subset[:]))
        return
    subset.append(arr[i])
    recursion(i+1,n,subset,arr)
    subset.pop()
    recursion(i+1,n,subset,arr)
    
arr=[1,2,2]
length=len(arr)
res=set()
subset=[]
recursion(0,length,subset,arr)
finalres = [list(sub) for sub in res]
finalres.sort()
print(finalres)
