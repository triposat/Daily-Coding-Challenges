class Node:
    def __init__(self):
        self.child = {}
        self.cnt = 0


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        root = self.root
        for c in word:
            root = root.child.setdefault(c, Node())
        root.cnt = 1

    def search(self, word: str) -> bool:
        root = self.root
        for c in word:
            if c not in root.child:
                return False
            root = root.child[c]
        return root.cnt

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for c in prefix:
            if c not in root.child:
                return False
            root = root.child[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)