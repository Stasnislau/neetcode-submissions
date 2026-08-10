class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rl = len(matrix[0])
        cl = len(matrix)
        l = 0
        r = rl * cl - 1
        while l <= r:
            mid = (l + r) // 2
            midr = mid // rl
            midc = mid % rl 

            if matrix[midr][midc] == target:
                return True
            elif matrix[midr][midc] > target:
                r = mid - 1
            else:
                l = mid + 1
            
        return False