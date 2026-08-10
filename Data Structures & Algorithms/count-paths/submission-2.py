class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for y in range(1, m):
            new_row = [1] * n
            for c in range(1,n):
                new_row[c] = row[c] + new_row[c-1]
            row = new_row
        return row[n-1]
                
        