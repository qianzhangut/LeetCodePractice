class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        un={}
        for i in nums:
            if i not in un:
                un[i] = 1
            else:
                un[i] +=1
        return list(un.keys())[list(un.values()).index(1)]

##bitwise exclusive or
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
    res = nums[0]
    for i in nums[1:]:
        print(res, i)
        res ^= i
        print(res)