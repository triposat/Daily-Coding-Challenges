class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        hmap = {}
        ans = []

        def change(char):
            if char not in hmap:
                hmap[char] = chr(97+len(hmap))
            return hmap[char]

        def replace(word):
            hmap.clear()
            for i in range(len(word)):
                if change(word[i]) != cipher[i]:
                    return
            ans.append(word)

        cipher = [change(char) for char in pattern]
        for word in words:
            replace(word)
        return ans