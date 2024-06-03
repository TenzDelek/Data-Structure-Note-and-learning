#print name 5 times---------------------------
# def nameprint(i,n):
#     if(i>n):
#         return
#     print("i am tenzin")
#     nameprint(i+1,n)
# nameprint(1,5)

#print linearly from 1 to n--------------------
# def linear(i,n):
#     if(i>n):
#         return
#     print(i)
#     linear(i+1,n)

# linear(1,5)

#print from n to 1------------------------

# def reverse(i,n):
#     if(n<i):
#         return
#     print(n)
#     reverse(i,n-1)
# reverse(1,5)

#printing from 1 to n with backtracking-------------
# def backtrack(i):
#     if(i<1):
#         return
#     backtrack(i-1)
#     print(i)

# backtrack(3)

#printing from n to 1 with backtracking-------------
# def reverseprint(i,n):
#     if(i>n):
#         return
#     reverseprint(i+1,n)
#     print(i)
# reverseprint(1,5)

#sum of n number-------------------------------

# def sumn(n,sum1):
#     if(n==0):
#         print(sum1)
#         return

#     sumn(n-1,sum1+n)
# sumn(3,0)

#sum using function------------------------

# def sumn(n):
#     if(n==0):
#         return 0
#     return n+sumn(n-1)
# output=sumn(3)
# print(output)

#factorial-------------------
# def fact(n):
#     if(n==1):
#         return 1
#     return n*fact(n-1)
# facto=fact(10)
# print(facto)
