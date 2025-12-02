class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        '''temp=None
        si,ei=-1,-1
        s=0
        e=len(nums)-1
        while s<=e:
            mid=(s+(e-s))//2
            if nums[mid]==target:
                si,ei=mid,mid
            elif target<nums[mid]:
                e=mid-1
            else:
                s=mid+1
        while(si>0 and nums[si-1]==target):
            si-=1
        while (ei<len(nums)-1 and nums[ei+1]==target):
            ei+=1
        return [si,ei]'''

        if target in nums:
            return [nums.index(target),len(nums)-1-nums[::-1].index(target)]
        else:
            return [-1,-1]


       

       