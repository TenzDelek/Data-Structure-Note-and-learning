# # summation of first n number
# #n=3 1+2+3=6

# def firstn(i,n,sm):
#     if(i>n):
#         print(f'the sum of the first {n} number is {sm}')
#         return
#     sm+=i
#     firstn(i+1,n,sm)
# n=int(input("enter the nth:"))
# firstn(1,n,0)

# #functional way (the importance of return)

# def func(n):
#     if(n==0):
#         return 0 #base case return 0
    
#     return n+ func(n-1) #remember return

# print(func(3))
    
# #factorials
# def fact(n):
#     if(n==1):
#         return n #imp
#     return n * fact(n-1)
# print(fact(3))