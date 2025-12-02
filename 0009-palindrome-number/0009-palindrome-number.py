class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x<10:
            return True
        else:
            temp=x
            rev=0
            ld=0
            while temp!=0:
                ld=temp%10
                rev=rev*10+ld
                temp=temp//10
            if rev==x:
                return True
            else:
                return False
        