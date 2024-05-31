# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            if curr.val > q.val and curr.val > p.val:
                curr = curr.left
            elif curr.val < q.val and curr.val < p.val:
                curr = curr.right
            else:
                return curr

        