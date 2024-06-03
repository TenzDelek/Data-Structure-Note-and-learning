# shell is created by calling python in terminal
crtl + Z to go out of the shell
shell--------
import os
os.getcwd()-> gives the current working directory

import sys
sys.platform ->gives the platform win32

in shell you can import your file like tenzin.py by
import tenzin
now you can use its function by calling it filename then the function
tenzin.chai("tenzindelek")

# problem in python and its solution (shell)
so incase you have imported the file then you run the function and all
but after a while you go to that file and create a new vairable like chai_one
and all. 
so now when you try to access it in the shell it will say there is no attribute like chai_one. why?
because the shell doesnt know that the main file(tenzin.py) is changed. so to fix that
import a lib name (from importlib import reload). now we can call the reload
like reload(filename)
and so the changes will be reflect in the shell

# mutable and non mutable
you may have wonder about that when
we create a variable
name="tenzin" <br>
print(name) -> this prints the tenzin
<br>
so now when we change <br>
name="delek"
it will not generate error but why isnt python string mutable yes it is so why can we change it. this all lies in the working of internal of the system.
python in general works in object base. so when u say username='tenzin'
it store tenzin as the object in the internal system not username. so the user name have the reference to the tenzin object. now when we say username="delek", we create the object delek in the internal system and point the reference to delek. and now <b> AS PYTHON HAS AUTOMATIC GARBAGE COLLECTOR</b> it remove the object which has no reference to its.

# OBJECT TYPE / DATA TYPE
- number : 123,3.12,3+4j, 0b111,Decimal(),fraction()
- string: 'tenzin',"bob's", b'a\x01c', u'sp\xc4m'
- list: [1,2[3,'three']], list(range(10))
- tuple: (1,'spam',3), tuple('spam'),namedtuple
- dictonary: {"food":'kichi','taste':'good'},
dict(hours=10)
- Set: set('abc'), {'a','b','c'}
- file: open('egg.txt'),open(r'C:\et','wb')
- Boolean : True, False
- None : None
- functions, module, classes

- Advance: Decorators, generators, iterators , 
metaprogramming

# some librarys
import math 
math.pi
import random
random.random()
random.choice([1,2,3,4])-> from that array only random will generated

# some functions
when we write username[-1]
its give the last value -2 gives the second last 
slicing : username[1:2] -> the last one is not included 
dir(username)-> gives the function we can perform to the vairable


#interview based
when we say a=2 we are not allocating the datatype to a we are just referencing that to a
the datatype is there in memory stored which here is 2 so now when we do a="tenzin" the 2 is free right. and you may think it automaticlly goes in garbage collection. 

yes it does but not immediately. as in python the string and the number are widely used, it is not collected immediately(late garbage collection)

# list working 
when we do l1=[1,2,3]
then l2=l1
both will be same 
now if you change l1[0]=32
it will be reflect in l2

but-----------wait
if we do p1=[1,2,3]
and p2=p1
but here again we say p2=[1,2,3]
now even if you change p1[0]=1212
it wont be reflect in p2 as p2 has it own new
memory as list is mutable it creates it own memory

# slicing trick for copying
h1=[1,2,3]
h2=h1[:]-> here if we dont give any it says from start to end 
but here there is a difference here between 
saying h2=h1 and h2=h1[:]
when we say h2=h1 we are referecning it to h1 directly so the changes will be reciprcate with it but when we say h2:h1[:] we are making a copy of it. so the changes will not be reflected

# is and ==
when we say l==r
it will give true or false
when we say l is r -> it checks the memory also so we can above h2:h1[:] 
h2 is h1 its give false as the memory is different but when we say
h1==h2 it will give true as values are same

# repr str and print

 repr('Hello, world!')
"'Hello, world!'"
str('Hello, world!')
"Hello, world!"
The repr() string is more unambiguous and can be used to recreate the object, while the str() string is more human-readable.

# and

1<2<3
similar to 1<2 and 2<3 -> true
1==2<3
1== 2 and 2<3 -> ans-false

# floor and ceil and trune
import math
math.floor(3.9) -> 3
math.floor(-3.5)->-4
- trune will bring toward 0
math.trune(2.8)->2
math.trune(-2.8)->-2

# octal,hexa and binary
0o20 ->16
0xFF ->255
0b1000->8
- in real day to day we dont need to memories these. we have fucntion
oct(64) hex(64) bin(64)
or we can use int to do so

int('64',8) -octal
int('64',16) -hexa
int('10000',2) -binary

# bitwise
x=1
x<<2 ->left shift by 2
ans->4


# random
import random
random.random() ->0.34345243
or we can say
random.randint(1,100)->100 not inclusive
or
arr=['tenzin','fss','efsefs']
random.choice(arr)
- shuffle
random.shuffle(arr)
now the value inside arr will change place(shuffle)

# decimal problem
when we do 0.1+0.1+0.1 it gives 0.300000..4
then when we subtract 0.1+0.1+0.1-0.3 here it gives problem like 5.55143 which shouldnt be it should be 0 right. even using bracket it wont work. so we use libary
from decimal import Decimal
Decimal('0.1')+Decimal('0.1')+Decimal('0.1')
will give Decimal('0.3') and subtracting that with Decimal('0.3') will give proper Decimal('0.0') 

# set
setone= {1,2,3,4}
setone & {1,3} ->gives the intersection(same element)
setone | {1,3,7} ->gives the unioon(all unique)
 
 # keypoint
 empty set are not define by {} it is define by set() 
 the {} is for dictonary

 # bool
 True is treated as 1
 so True+5 will give 6

 # strings
 name="Tenzin"
 print(name.lower()) all lower
 print(name.upper()) all upper

 chai="  tenzin  "
 print(chai.strip())-> removes all spaces

 name2="tenzin delek"
 print(name2.replace("tenzin","stanzain"))

name4="masala chai"
print(name4.find("chai"))
will give the first index of chai which here is 7 

name5="tenzin delek delek delek"
print(name5.count("delek"))
give the count of the string ->3

 # string to arr
 chai-"lemn, tet, tet, mint"
 print(chai.split(", "))->split based on , and space so it will print as
 ['lemn','tet','tet','mint']
also we can join
te=['t','e']
print("".join(te))-> ans te

# placeholder {}
type="masala"
quantity=3
order="i order {} cups of {} chai" ->the {} act as the placeholder
print(order.format(quantity,type))
will give i order 3 cups of masala chai

# the issue with ""
chai ="he said"tenzin is best" "
here it shows error we can solve it using making one of them single quote but the other way is  using  backslash which makes it not consider as string
chai ="he said\"tenzin is best\" "

# another issue with \n (raw)
when we say
name="tenzin\ndelek"
printing that will result in new line but we want it same line so we use raw
name=r"tenzin\ndelek"
now the printing is in same line as it is treated as raw string 
usefull in pathname

# list

.append("tenzin")->at last it add
.pop() ->pop from last
.remove("tenz")->remove from anywhere
.insert(1,"tenz")->add at any pos , the first parameter is the position and the second is the value to be added. in the array, the values will be shifted and the inserted value will be added

arr=arr1 ->here the array reference will be same, sometimes its create issue

we do 
arr=arr1.copy() or arr1[:] ->here new memory is created

# dictonary
name={"tenzin":"good","delek":"vgood"}
>>> name
{'tenzin': 'good', 'delek': 'vgood'}
>>> name.get("tenzin")
'good'
>>>name["delek"]
'vgood'
for i in name:
...     print(i, name[i])
...
tenzin good
delek vvvgod
same as
for key,val in name.items():
...     print(key,val)
...
tenzin good
delek vvvgod
- while poping we have to pass the key
name.pop("tenzin")
'good'
>>> name                         
{'delek': 'vvvgod'}
- the popitem() pops the last
name
{'delek': 'vvvgod', 'newlyadded': 'yoo'}
>>> name.popitem()
('newlyadded', 'yoo')
>>> name
{'delek': 'vvvgod'}

- or we can use
del name["value"]

- dictonary comprehension
sq={x:x**2 for x in range(6)}
>>> sq
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

- to clear dict
name.clear()
makes the dict empty ={}
- assigning the array to dict
keys=["tenzin","delek","senpai"]
>>> keys
['tenzin', 'delek', 'senpai']
>>> defaultval="good"
>>> newdict=dict.fromkeys(keys,defaultval)
>>> newdict
{'tenzin': 'good', 'delek': 'good', 'senpai': 'good'}  

# tuple
- cant be change 
represented with ()

# getting to know type
we can use type() to know the type

# count
we have 
arr=[1,2,3]
arr.count(1) -> how many 1 are there

# python 101

iteration tools-
for, comprehension
iterable objects-
list,file

# files
f=open('chai.py')
f.readline()->read line by line
f.__next__() ->raw way of doing above

or we can loop in it using
for line in open('chai.py'):
    print(line)
- this will print all
we can do the same using while
while True:
    line=f.readline()
    if not line:break
    print(line,end="")
will give the same result as the for loop

# iter()
>>> mylist=[1,2,3,4]
>>> I=iter(mylist)
>>> I
<list_iterator object at 0x000002BF755AAC20>
the I is point at the list that we create
points at first element ,
the memery reference will always point at first <object at 0x000002BF755AAC20>->never change
- here we can also use next(I) but using __ is more prefer in interview
>>> I.__next__()
1
>>> I.__next__()
2
>>> I.__next__()
3
>>> I.__next__()
4
>>> I.__next__()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration

but the pointing at same
>>> I
<list_iterator object at 0x000002BF755AAC20>

but in file we dont have to assign the ref
f=open('chai.py')
iter(f)
so when we do iter(f) is f it will give true
but for same
mylist=[1,2,3]
iter(mylist) is mylist it will give false 
as only we give the ref then it is iterable

# dict is also iterable also range is iterable

R=range(5)
I=iter(R)
next(I) -> it will go from starting

# lambda -> think of it like a another way of writing a function
use for lightweight -
cube=lambda x :x**3
print(cube)

# astrict * which is used for taking multple args (handle any number of arguement)
def sum1(*args):->here instead of args we can write any but args is better to write
  print(sum(args)) ->the arg comes in tuples ->so it is iterable we can use loop on arg

sum1(1,2,3)
sum1(1,2,4,5,6)
so as we have taken * it is now doesnt matter how much arguement we take it will take without error

# double astrict (kwargs) for key value pair

def print_kwargs(**kwargs):
  for key,value in kwargs.items():
    print(f"{key}: {value}")

print_kwargs(name="tenzin",power="lazer")
print_kwargs(name="tenzin")
print_kwargs(name="tenzin",power="lazer",enemy="dr.jack")

# yeild ->return value and also store in memory and its state

def evengenerator(limit):
  for i in range(2,limit+1,2):
    yeild i  # if we write return here it will create error

for num in evengenerator(10):
  print(num)
it will print 2,4,6,8,10

# scope and closure
- scope in python is term as namespace

so imagine your function scope as similar to creating a house in world. the world here is the global scope. now the variable tenzin in function (house) is not related to the tenzin vairable out in the world. the house(vairable) is only used in his house(function)

x=99
def func3():
  global x ->bring the global reference of x in function
  x=12
func3()
print(x)-> it will print 12
but we shouldnt override a global variable in the function scope

# understanding closure (factory function)- function that returns a class

def f1():
  x=99
  def f2():
    print(x)
  return f2
myres=f1()
myres() ->will print 99 
when we return the f2 ref it stores in the myres but in my res when we print it the reason why it perfectly gives the correct value is that when we store the memory reference of f2 we also store the x value associated with it. (that is call closure)
not only the definition(fn) goes , the associated vairable reference also goes in


def tenzincode(num):
  def actual1(x):
    return x**num
  return actual
f=tenzincode(2) ->f has the actual1 function

now when we do 
print(f(3))-> the 3 is the one which actual1 need. so the answer will be 3**2 =9