class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        g, m, p = 0, 0, 0
        total = 0
        for i in range(len(garbage)):
            for char in garbage[i]:
                if char == 'G':
                    g = i
                elif char == 'M':
                    m = i
                else:
                    p = i
                total += 1
        for i in range(1, len(travel)):
            travel[i] = travel[i-1]+travel[i]
        if g:
            total += travel[g-1]
        if p:
            total += travel[p-1]
        if m:
            total += travel[m-1]
        return total