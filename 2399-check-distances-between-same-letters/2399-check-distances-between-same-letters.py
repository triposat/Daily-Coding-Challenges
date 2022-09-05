class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        freq=defaultdict(list)
        for i in range(len(s)):
            freq[s[i]].append(i)
        print(freq)
        flag=False
        for key in freq:
            if not distance[ord(key)-ord('a')]==freq[key][1]-freq[key][0]-1:
                flag=True
        if flag:
            return False
        return True