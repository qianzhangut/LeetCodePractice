class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        numVal = 0
        length = len(nums)
        p = 0
        while p < length - numVal:
            if nums[p] == val:
                nums[p] = nums[length - 1 - numVal]
                numVal += 1

            else:
                p += 1

        return length - numVal