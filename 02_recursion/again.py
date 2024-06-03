# def print5time(n):
#     if(n==0):
#         return
#     print("hello")
#     print5time(n-1)
#     print(f'i got backtrack at {n}') # the backtrack rememeber it like a stack when 5 is pass it goes in a 
#     #stack then 4 is call it goes in , and at 1 when it reach the base case, now as stack, the top goes out first (lifo) so 1 to 5
#     #or
#     # you can remember it like the 5 call is not finish yet so it waiting
#     # thats why when there is no base case the problem of stack overflow or the segmentation error occurs
# print5time(5)

# # the base case can be any thing like

# def predictmyname(counter):
#     if(counter==5):
#         print("bro you dont know my name")
#         return
#     name=input("predict my name: ")
#     if name =="tenzin":
#         print("yes sir")
#         return
#     counter+=1
#     predictmyname(counter)
# counter=0
# predictmyname(counter)

# # the space complexity is taken of the stack
# # O(n) also the time complexity is O(n)
# def name(n,limit):
#     if(n==limit):
#         return
#     print("tenzin")
#     name(n+1,limit)
# limit=int(input("enter limit:"))
# name(0,limit)

# #1 to n
# def linear(i,n):
#     if(i>n):
#         return
#     print(i)
#     linear(i+1,n)
# n=int(input("enter your limit:"))
# linear(1,n)

# #n to 1

# def revlinear(n):
#     if(n==0):
#         return
#     print(n)
#     revlinear(n-1)
# n=int(input("enter the limit:"))
# revlinear(n)

# #printing 1 to n but in backtrack
# #so we go from 5 to 1 then when backtrack we 
# #print from 1 to 5

# def oneback(n):
#     if(n==0):
#         return
#     oneback(n-1)
#     print(n) # print 1 to 5 as it is backtrack
# oneback(5)

#printing n to 1 but in backtrack

# def backtwo(n,target):
#     if(n>target):
#         return
#     backtwo(n+1,target)
#     print(n)
# target=int(input("enter limit: "))
# backtwo(1,target)