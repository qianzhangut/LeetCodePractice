class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:


        return [max(len(str(i)) for i in j) for j in zip(*grid)]

      