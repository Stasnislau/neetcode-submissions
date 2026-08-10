class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque() # храним ИНДЕКСЫ

        for r in range(len(nums)):
            # 1. Выкидываем из конца всё, что меньше текущего (они мусор)
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # 2. Выкидываем из начала элемент, если он вылетел за левый край окна
            if q[0] < r - k + 1:
                q.popleft()
                
            # 3. Если окно достигло размера k, пишем ответ (максимум всегда в q[0])
            if r >= k - 1:
                res.append(nums[q[0]])
                
        return res