list1=[1,2,3,4]
lsit2=[5,6,7,8,10] #even it has 5 the zip stops at smaller length so the 10 is not
#used

for item in zip(list1,lsit2):
    print(item)