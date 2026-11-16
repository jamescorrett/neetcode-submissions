class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix) - 1, len(matrix[0]) - 1

        top, bot = 0, rows
        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            elif matrix[mid][0] <= target <= matrix[mid][-1]:
                targetRow = mid
                break
        else:
            return False

        l, r = 0, cols

        while l <= r:
            m = (l + r) // 2
            if matrix[targetRow][m] < target:
                l = m + 1
            elif matrix[targetRow][m] > target:
                r = m - 1
            elif matrix[targetRow][m] == target:
                return True

        return False
        

            

        


            
            
            