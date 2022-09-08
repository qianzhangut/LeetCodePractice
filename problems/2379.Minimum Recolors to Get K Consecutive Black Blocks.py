class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = numw = blocks[:k].count("W")
        
        for i in range(k, len(blocks)):
            if blocks[i] == "W":
                numw += 1
            if blocks[i - k] == "W":
                numw -= 1
            ans = min(ans, numw)
        return ans
            