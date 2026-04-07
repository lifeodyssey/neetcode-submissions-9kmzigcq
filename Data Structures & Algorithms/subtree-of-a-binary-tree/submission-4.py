# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isSameTree(root,subRoot):
            return True
        if not root and not subRoot:
            return True
        stack=[root]
        while stack:
            node=stack.pop()
        
            if node.left:
                if self.isSameTree(node.left,subRoot):
                    return True
                else:
                    stack.append(node.left)
            if node.right:
                if self.isSameTree(node.right,subRoot):
                    return True
                else:
                    stack.append(node.right)
        return False
        
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
