class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        res, max_cnt = 1e9, -1

        for d in divisors:
            cnt = 0
            for x in nums:
                if x%d == 0:
                    cnt += 1
            if cnt>max_cnt:
                res = d
                max_cnt=cnt
            elif cnt == max_cnt:
                res = min(res, d)
        return res
                