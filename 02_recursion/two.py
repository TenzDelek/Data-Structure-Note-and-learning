# sum of n 
#usning parameter
# def summ(i,summm):
#     if(i<1):
#         print(summm)
#         return
#     summ(i-1,summm+i)

# summ(3,0)

#using function

# def sumn(n):
#     if(n==0):
#         return 0
#     return n+sumn(n-1)
# res=sumn(3)
# print(res)


#reversing a arr
# def reverse1(i,n,arr):
#     if(i>=n/2):
#         return
#     arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
#     reverse1(i+1,n,arr)
     
    
# arr=[1,2,3,4]
# n=len(arr)
# reverse1(0,n,arr)

# print(arr)

#checking for palindrome

def palindrome(i,n,s):
    if(i>=n/2):
        return True
    if(s[i]!=s[n-i-1]):
        return False
    return palindrome(i+1,n,s)
s="madam"
n=len(s)
res=palindrome(0,n,s)
print(res)