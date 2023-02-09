class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        s = [(w[0] in 'aeiou') and (w[-1] in 'aeiou') for w in words]
        pre = [0]
        total = 0
        for i in s:
            total += i
            pre.append(total)

        return [pre[q[-1]+1] - pre[q[0]] for q in queries]