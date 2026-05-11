class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        mid = 0
        high = len(matrix) - 1

        #STEP 1 -- Binary search on first column 
        while low <= high:
            if(low == high and matrix[low][0] > target):
                break
            mid = low + ((high - low) // 2)
            if(matrix[mid][0] == target):
                return True
            elif (target < matrix[mid][0]):
                high = mid - 1
            else:
                low = mid + 1

        #STEP 2 -- Binary search on defined row
        print(f"Selected row is {mid}")
        row = mid
        low = 0
        mid = 0
        high = len(matrix[row]) - 1
        while low <= high:
            mid = low + ((high - low) // 2)
            print(f"New mid index is {mid}")
            if(matrix[row][mid] == target):
                return True
            elif (target < matrix[row][mid]):
                high = mid - 1
            else:
                low = mid + 1

        return False

