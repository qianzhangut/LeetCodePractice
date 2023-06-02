class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        res = sorted(prices)

        return money if sum(res[:2])>money else money-sum(res[:2]) 