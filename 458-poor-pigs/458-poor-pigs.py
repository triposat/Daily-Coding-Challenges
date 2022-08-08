class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        time = minutesToTest//minutesToDie+1
        pigs = 0
        while time**pigs < buckets:
            pigs += 1
        return pigs