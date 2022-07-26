class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cols = Counter(tuple(zip(*grid)))
        rows = Counter(map(tuple, grid))
        return sum(rows[lst]*cols[lst] for lst in rows)