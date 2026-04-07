# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        a,b=p.val,q.val
        while root:
            if a<root.val and b<root.val:
                root=root.left
            elif a >root.val and b>root.val:
                root=root.right
            else:
                return root