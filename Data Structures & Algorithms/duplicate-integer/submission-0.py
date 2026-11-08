class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        numList = []
        duplicateList = []
        
        for num in nums: 
            if num in numList:
                duplicateList.append(num)
            else:
                numList.append(num)
            
        if len(duplicateList) > 0:
            return True

        else:
            return False