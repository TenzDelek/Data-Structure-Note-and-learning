'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

'''
# the keypoint is that it needs its data of its location so make changes as per it
class Tenzin:
    def letgo(self,arr:list,target:int)->list:
        modifyarr=[[val,index] for index,val in enumerate(arr)]
        modifyarr.sort()
        l=0
        r=len(arr)-1
        while(l<r):
            value=modifyarr[l][0]+modifyarr[r][0]
            if(value==target):
                return [modifyarr[l][1],modifyarr[r][1]]
            elif(value>target):
                r-=1
            else:
                l+=1
if __name__=="__main__":
    obj=Tenzin()
    ans=obj.letgo([3,2,4],6)
    print(ans)

'''
there is another way we used the thought process where if the difference is in array(hash) we return it.
but the current method is what comes in my mind when i see it so most probably this soln will come in my mind
when i give interview. the space and time complexity are same
'''