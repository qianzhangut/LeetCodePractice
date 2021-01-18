
## use sort
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = sorted(nums)
        now, big = 1, 1
        for i in range(1,len(n)):
            if n[i] != n[i-1]:
                if n[i] == n[i-1] +1:
                    now +=1
                else:
                    big = max(big, now)
                    now = 1
        return max(now, big)   


## use set look up o(1)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lon = 0
        num_set = set(nums)
        for num in num_set:
            if num-1 not in num_set:
                current_num = num
                now = 1
                
                while current_num +1 in num_set:
                    current_num += 1
                    now += 1
                    
                lon = max(lon, now)
                
        return lon       