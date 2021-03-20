class Solution:
    def removeDuplicates(self, S: str) -> str:
        ans=[]
        
        for i in S:
            if ans and ans[-1] == i:
                ans.pop()
            else:
                ans.append(i)
        return ''.join(ans)