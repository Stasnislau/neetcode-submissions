class CountSquares:

    def __init__(self):
        self.points = {}

    def add(self, point: List[int]) -> None:
        if (point[0], point[1]) in self.points:
            self.points[(point[0], point[1])] += 1
        else:
            self.points[(point[0], point[1])] = 1
        

    def count(self, point: List[int]) -> int:
        target_x, target_y = point
        res = 0
        for (x, y), count in self.points.items():
            if (x == target_x or y == target_y) or (abs(target_x - x) != abs(target_y - y)):
                continue

            corner1 = (target_x, y)
            corner2 = (x, target_y)
            if corner1 in self.points and corner2 in self.points:
                res += count * self.points[corner1] * self.points[corner2]


        return res


            
        
