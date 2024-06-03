#so a subsequence can be term as contigous and also non contigous which follows an order
#like for [1,2,3] the subseqence can be
#{}
#1 -contigoues
#2 -contigoues
#3 -contigoues
#1,2 -contigoues
#2,1 -contigoues
#1,3 -non-contigoues - elemet 2 is between 1 and 3 right
#123 -contigoues

#so for size of 3 n=3 the subsequence are 8
# now in the defination we have seen that "which follows an order" now what thats means is that
#we cant write like 3,2,1 as the order is not right. the order of the array should be maintain

# a empty set is also consider as subsequence

#important concept
#here this concept is essential, the method we can call it pick not pick, so basically what we are doing is
#making a recursion like tree for each pick and not pick. the index is the one that is incremented.

#the pick will perform first then not pick
def subsecfunc(index,subsec,arr,n):
    if(n==index):
        print(subsec)
        return
   
    subsec.append(arr[index]) #to find the pick
    subsecfunc(index+1,subsec,arr,n)#for pick
    subsec.pop() # to find the not pick
    subsecfunc(index+1,subsec,arr,n) #for not pick
   

arr=[1,2,3]
n=len(arr)
subsec=[]
index=0
subsecfunc(index,subsec,arr,n)

