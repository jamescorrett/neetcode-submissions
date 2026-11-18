class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minNum = nums[(l + r) // 2]
        while l <= r:
            m = (l + r) // 2
            if nums[m] >= nums[l] and nums[m] >= nums[r]:
                l = m + 1
                minNum = min(minNum, nums[m])

            else:
                r = m -1
                minNum = min(minNum, nums[m])

        return minNum
        
 