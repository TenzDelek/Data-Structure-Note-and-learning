# intersection of two array
'''
leetcode July 2nd
'''
class Delek:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:

        nums1.sort()
        nums2.sort()
        i,j=0,0
        res=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                res.append(nums1[i])
                j+=1
                i+=1
            elif(nums1[i]<nums2[j]):
                i+=1
            else:
                j+=1
        print(res)
        return res

if __name__=='__main__':
    obj=Delek()
    nums1=[4,9,5]
    nums2=[9,4,9,8,4]
    ress=obj.intersect(nums1,nums2)
    print("the answer is :")
    print(ress)
    


