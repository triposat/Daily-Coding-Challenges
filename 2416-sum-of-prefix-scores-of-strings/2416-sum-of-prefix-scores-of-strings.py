class Node:
    def __init__(self):
        self.child = {}
        self.cnt = 0
        
class Trie:
    def __init__(self):
        self.trie = Node()

    def insert(self, word):
        node = self.trie
        for ch in word:
            if ch not in node.child:
                node.child[ch] = Node()
            node = node.child[ch]
            node.cnt += 1

    def count(self, word):
        ans = 0
        node = self.trie
        for ch in word:
            ans += node.child[ch].cnt
            node = node.child[ch]
        return ans

class Solution:
    def sumPrefixScores(self, words):
        trie = Trie()
        for word in words:
            trie.insert(word)
        return [trie.count(word) for word in words]