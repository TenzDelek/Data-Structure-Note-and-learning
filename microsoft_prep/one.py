#kadane algo - the concept for the subarray sum
# def sub(arr):
#     maxsum=arr[0]
#     for i in range(len(arr)):
#         cursum=0
#         for j in range(i,len(arr)):
#             cursum+=arr[j]
#             maxsum=max(cursum,maxsum)
#     return maxsum

# arr=[-1,-2,-3,-4]
# ans=sub(arr)
# print(ans)

arr = [1,2,3,4,5]
newarr=[]
D=2
N=5
for i in range(D,N):
    newarr.append(arr[i])
        
for i in range(D):
    newarr.append(arr[i])
print(newarr)

            