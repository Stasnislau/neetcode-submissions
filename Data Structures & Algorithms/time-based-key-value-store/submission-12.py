from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.storage[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        val = self.storage[key]
        if not val:
            return ''
        l = 0
        r = len(val) - 1
        res = ''
        print(val)
        while l <= r:
            mid = (l + r) // 2
            print(mid,val[mid][0] )
            if val[mid][0] <= timestamp:
                res = val[mid][1]
                l = mid + 1 
            else:
                r = mid - 1
        return res
