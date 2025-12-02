class Solution:
    def reverse(self, x: int) -> int:
        if x<=-(2**31) or x>(2**31)-1:
            return 0
        ans=self.rev(abs(x))
        if ans>(2**31)-1 or -ans<=-(2**31):
            return 0
        if x<0:
            return -ans
        return ans




    def rev(self,x):
        r=0
        temp=0
        while x!=0:
            temp=x%10
            r=r*10+temp
            x=x//10
        return r
        