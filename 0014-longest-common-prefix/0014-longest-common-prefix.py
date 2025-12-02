class Trie:
    def __init__(self):
        self.dict={}
        self.flag=0
    def insert(self,s):
        t=self
        for char in s:
            if char not in t.dict:
                t.dict[char]=Trie()
            t=t.dict[char]
        t.flag=1
    def prefix(self,s):
        ans=""
        t=self
        for char in s:
            if len(t.dict)>1:
                return ans
            t=t.dict[char]
            ans+=char
        return ans

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        t=Trie()
        for word in strs:
            t.insert(word)
        return t.prefix(min(strs,key=lambda x: len(x)))
        