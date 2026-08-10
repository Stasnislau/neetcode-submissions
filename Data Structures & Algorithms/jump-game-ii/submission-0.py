class Solution:
    def jump(self, nums: List[int]) -> int:
        # Если массив из 1 элемента, мы УЖЕ на финише, прыгать не надо
        if len(nums) == 1:
            return 0
            
        jumps = 0          # Наш счетчик прыжков
        current_end = 0    # Граница ТЕКУЩЕГО прыжка (радиус взрыва гранаты)
        farthest = 0       # Самая дальняя точка, куда мы можем дотянуться СЛЕДУЮЩИМ прыжком
        
        for i in range(len(nums) - 1):
            
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:
                jumps += 1
                
                current_end = farthest
                
                if current_end >= len(nums) - 1:
                    break
                    
        return jumps
