add10= lambda x:x+10
print(add10(4)) #gives 14
#lambda is similar to a function -> used when u need only once in your code
#Like 
# def add10(x):
#     return x=x+10

#two args
mulxy=lambda x,y:x*y
print(mulxy(10,10))

#usage
#1.in sorting 2d array
arr=[[1,2],[10,1],[33,10],[13,4]]
# the normal .sort() doesnt work on 2darray
sortedarr=sorted(arr) #by default it sort based on first element like c cordinate here
print(sortedarr)

sortedarrbykey=sorted(arr,key= lambda x:x[1]) # x index1 is the y values
print(sortedarrbykey)

# if want to sort base on the sum of each
sortedarrbysum= sorted(arr,key= lambda x:x[0]+x[1])
print(sortedarrbysum)

#map in python map(func,seq)--------------------------

oo=[1,2,3,4,5]
res1=map(lambda x:x*2 ,oo) #multiply arr by 2
print(list(res1))

#can be done similar using list comprehension
res2=[x*2 for x in oo]
print(res2)

#filter in python filter(func,seq) --------------
#filter out things
ol=[1,2,3,4,5]
res3=filter(lambda x:x%2==0,ol) #gives only the even number
print(list(res3))
#also with list comphrension
res4=[x for x in ol if x%2==0]
print(res4)

from functools import reduce
#reduce in python reduce(func,seq) --------------
op=[1,2,3,4]
res5=reduce(lambda x,y: x*y,op) #gives only 1output used for multiplication like here
print(res5)