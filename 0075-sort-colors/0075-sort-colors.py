class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0=0
        count1=0
        count2=0
        for i in nums:
            if i==0:
                count0+=1
            elif i==1:
                count1+=1
            else:
                count2+=1
        nums[:count0]=[0]*count0
        nums[count0:count1+count0]=[1]*count1
        nums[count1+count0:len(nums)]=[2]*count2