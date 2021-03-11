class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        l, r = 0, len(S)
        ans=[]
        for i in S:
            if i == "I":
                ans.append(l)
                l += 1
            else:
                ans.append(r)
                r -= 1
        return ans+[l]