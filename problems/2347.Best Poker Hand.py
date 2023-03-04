class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        ans = "High Card"
        d = {}
        for i in ranks:
            d[i] = d.get(i, 0) + 1

        max_ranks = max(d.values())

        if len(set(suits)) == 1:
            return "Flush"
        elif max_ranks>=3:
            return "Three of a Kind"
        elif max_ranks>=2:
            return "Pair"
        return ans