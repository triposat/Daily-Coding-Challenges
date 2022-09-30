# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root):
        if not root:
            return None
        q = [root]
        level = 0
        while q:
            if level & 1:
                vals = [node.val for node in q]
                for node in q:
                    node.val = vals.pop()
            for _ in range(len(q)):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return root
