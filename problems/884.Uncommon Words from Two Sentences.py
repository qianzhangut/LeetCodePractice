class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        combo = (A + " " +B).split()
        count = {}
        for i in combo:
            count[i] = combo.count(i)
        return [i for i in count if count[i] == 1]