# for binary search the term like maximize, 
#minimize the maximum value, or maximize the minimum value , or find the maximum possible 
#value or find the minimum possible value is the key word you should be looking for.

#the fundamental of bin search is that the one part will be no use

#note that the element should be sorted before checking the res as mention above
class Delek:
    def tenzin(self,arr:list[int],target:int)->int:
        l=0
        r=len(arr)-1
        arr.sort()
        while(l<=r):
            mid=l+(r-l)//2
            if(arr[mid]==target):
                return mid
            elif(arr[mid]>target):
                r=mid-1
            else:
                l=mid+1
        return -1
if __name__== "__main__":
    arr=[]
    n=int(input("enter the length: "))
    for i in range(n):
        num=int(input("enter the num: "))
        arr.append(num)
    target=int(input("what is the target: "))
    obj=Delek()
    res=obj.tenzin(arr,target)
    if res==-1:
        print("the target is not found i guess")
    else:
        print(f'so the answer is {res} ')




