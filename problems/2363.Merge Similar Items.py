#counter value and weight
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        cnt = Counter()
        for v, w in items1 + items2:
            cnt[v] += w
        return sorted(cnt.items())
# cleaner version
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:   
		cnt = Counter(dict(items1))
		cnt += Counter(dict(items2))
		return sorted(cnt.items())