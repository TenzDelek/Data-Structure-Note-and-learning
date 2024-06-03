#for the overall printing-----------------------
# arr=[1,2,1]
# n=len(arr)
# subarr=[]

# def subfunction(i,subarr,arr,n):
#     if(i==n):
#         print(subarr)
#         return
#     subarr.append(arr[i])
#     subfunction(i+1,subarr,arr,n)
#     subarr.pop()
#     subfunction(i+1,subarr,arr,n)

# subfunction(0,subarr,arr,n)

#overall printing but in reverse ---------------------------
# arr=[1,2,1]
# n=len(arr)
# subs=[]
# def subfunc(i,subs,arr,n):
#     if(i==n):
#         print(subs)
#         return 
#     subfunc(i+1,subs,arr,n)
#     subs.append(arr[i])
#     subfunc(i+1,subs,arr,n)
#     subs.pop()
    
# subfunc(0,subs,arr,n)

# printing subsequence whose sum matches the target------------------

# arr=[2,3,6,7]
# target=7
# subar=[]
# n=len(arr)
# sum1=0
# def myfunc(i,subar,target,n,arr,sum1):
#     if(i==n):
#         if(sum1==target):
#             print(subar)
#         return
#     subar.append(arr[i])
#     sum1+=arr[i]
#     myfunc(i+1,subar,target,n,arr,sum1)
#     subar.pop()
#     sum1-=arr[i]
#     myfunc(i+1,subar,target,n,arr,sum1)

# myfunc(0,subar,target,n,arr,sum1)

#printing the match sum just one time (can use flag but dont)---------------------
#pick notpick plus true and false game

# arr=[1,2,1]
# subarr=[]
# n=len(arr)
# target=2
# sum1=0

# def myfunc(i,arr,subarr,n,target,sum1):
#     if(i==n):
#         if(target==sum1):
#             print(subarr)
#             return True
#         else:
#             return False
    
#     subarr.append(arr[i])
#     sum1+=arr[i]
#     if(myfunc(i+1,arr,subarr,n,target,sum1)==True):
#         return True
#     sum1-=arr[i]
#     subarr.pop()
#     if(myfunc(i+1,arr,subarr,n,target,sum1)==True):
#         return True
#     return False

# myfunc(0,arr,subarr,n,target,sum1)


#now Regarding the count based problems------------------------------
#here the return is of 0 and 1

# arr=[1,2,1]
# n=len(arr)
# sum1=0
# target1=2
# def myfunc(i,arr,sum1,target1):
#     if(i==n):
#         if(target1==sum1):
#             return 1
#         else:
#             return 0
#     sum1+=arr[i]
#     l=myfunc(i+1,arr,sum1,target1)
#     sum1-=arr[i]
#     r=myfunc(i+1,arr,sum1,target1)

#     return l+r

# print(myfunc(0,arr,sum1,target1))