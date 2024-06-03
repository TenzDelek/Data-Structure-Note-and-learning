#swapping using the recursion
# the basic l and r

# #or can use the formula of n-i-1
# def swap(l,r,arr):
#     if(l>=r):
#         print(arr)
#         return
#     arr[l],arr[r]=arr[r],arr[l]
#     swap(l+1,r-1,arr)
# arr=[1,2,3,4]
# length=len(arr)-1
# swap(0,length,arr)

# #using the formula of n-i-1
# #we can find a palindfrome or not
# #time complexity is O(n/2) only half we are visiting

# def palin(i,s,n):
#     if(i>=n//2):
#         return True
    
#     if(s[i]!=s[n-i-1]):
#         return False
    
#     return palin(i+1,s,n)
# s="madam"
# print(palin(0,s,len(s))) #here the reason why len-1 is not needed is 
# #that in line 22 we are doing that explicitly

