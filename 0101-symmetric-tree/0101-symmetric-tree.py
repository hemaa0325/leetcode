# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        def same(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False

            return (
                p.val == q.val
                and same(p.left, q.right)
                and same(p.right, q.left)
            )

        return same(root.left, root.right) if root else True

        return same(root.right,root.left) if root else True