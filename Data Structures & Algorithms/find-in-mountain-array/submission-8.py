class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        
        l, r = 0, n - 1
        peak_idx = 0
        while l < r:
            mid = (l + r) // 2
            if mountainArr.get(mid) < mountainArr.get(mid + 1):
                l = mid + 1 
            else:
                r = mid 
        peak_idx = l 
        
        
        l, r = 0, peak_idx
        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
                
        l, r = peak_idx + 1, n - 1
        while l <= r:
            mid = (l + r) // 2
            val = mountainArr.get(mid)
            if val == target:
                return mid
            elif val > target:
                l = mid + 1
            else:
                r = mid - 1
            

        return -1

