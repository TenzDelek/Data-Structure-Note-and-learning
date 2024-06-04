
class Node:
    def threesum(self,arr:list[int],n:int):
        res=set()
        for i in range(0,n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if(arr[i]+arr[j]+arr[k]==0):
                        print("i got in")
                        res.add((arr[i],arr[j],arr[k]))
        print(arr)
        print(n)
        print(res)



if __name__ =='__main__':
    n=int(input("enter the length: "))
    inputarr=[]
    for i in range(n):
        val=int(input(f"enter the value at position {i} :"))
        inputarr.append(val)
    node=Node()
    node.threesum(inputarr,n)


