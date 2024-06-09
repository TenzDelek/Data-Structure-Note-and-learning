class Delek:
    def prefixsum(self,arr:list[int]):
        prefix=[0]*(len(arr)+1)
        for i in range(1,len(arr)+1):
            prefix[i]=prefix[i-1]+arr[i-1]
        
        return prefix
        

if __name__=="__main__":
    n=int(input("enter the array length: "))
    arr=[]
    for i in range(n):
        val=int(input(f"enter the value for {i}th place :"))
        arr.append(val)
    obj=Delek()
    res=obj.prefixsum(arr)
    print(res)
