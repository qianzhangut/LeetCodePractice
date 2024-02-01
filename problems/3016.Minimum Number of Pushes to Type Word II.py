from collections import Counter

class Solution:
    def minimumPushes(self, s: str) -> int:
        m = Counter(s)
        v = sorted(m.values(), reverse=True)
        ans = 0
        for i in range(1, len(v) + 1):
            if i <= 8:
                ans += v[i - 1]
            if 8 < i <= 16:
                ans += v[i - 1] * 2
            if 16 < i <= 24:
                ans += v[i - 1] * 3
            if i > 24:
                ans += v[i - 1] * 4
        return ans