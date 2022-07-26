class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = Counter(t)
        tarlen = len(t)
        start = 0
        validWin = ""
        for end in range(len(s)):
            if target[s[end]] > 0:
                tarlen -= 1
            target[s[end]] -= 1
            while tarlen == 0:
                window = end-start+1
                if not validWin or window < len(validWin):
                    validWin = s[start:end+1]
                target[s[start]] += 1
                if target[s[start]] > 0:
                    tarlen += 1
                start += 1
        return validWin