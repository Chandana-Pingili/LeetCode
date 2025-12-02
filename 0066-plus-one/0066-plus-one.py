class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=""
        for i in digits:
            s=s+str(i)
        s=int(s)
        return list(map(int,str(s+1)))
        