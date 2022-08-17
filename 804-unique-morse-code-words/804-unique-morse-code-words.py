class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        table = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        res = set()
        for word in words:
            empS = ''
            for char in word:
                empS += table[ord(char)-ord('a')]
            res.add(empS)
        return len(res)
