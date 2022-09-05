class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        freq=defaultdict(list)
        for i in range(len(s)):
            freq[s[i]].append(i)
        
        for char, (a, b) in freq.items():
            if not b-a-1 == distance[ord(char)-ord('a')]:
                return False
        return True