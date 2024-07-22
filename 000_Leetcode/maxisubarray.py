class Tenzin:
    #TLE
    def subarr(self,nums:list[int])->list[int]:
        totalsum=-float('inf')
        for i in range(len(nums)):
            cursum=0
            for j in range(i,len(nums)):
                cursum+=nums[j]
                totalsum=max(totalsum,cursum)
        return totalsum

if __name__=="__main__":
    obj=Tenzin()
    res=obj.subarr([-2,1,-3,4,-1,2,1,-5,4])
    print(f"the answer to this is:{res}")
        
