class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minNum = nums[(l + r) // 2]
        while l <= r:
            m = (l + r) // 2

            if nums[l] < nums[r]:
                minNum = min(minNum, nums[l])
                break

            elif nums[m] >= nums[l]:
                l = m + 1
                minNum = min(minNum, nums[m])

            else:
                r = m -1
                minNum = min(minNum, nums[m])

        return minNum
        
 