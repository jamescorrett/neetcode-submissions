class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2

            if target == nums[m]:
                return m

            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    #move right
                    l = m + 1
                else:
                    #move left
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    #move left
                    r = m - 1
                else:
                    #move right
                    l = m + 1

        return -1