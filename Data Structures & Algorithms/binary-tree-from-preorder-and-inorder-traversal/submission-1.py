# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        root=TreeNode(preorder[0])
        k=inorder.index(root.val)
        leftInorder=inorder[0:k]
        rightInorder=inorder[k+1:]
        leftsize=len(leftInorder)
        leftPreorder=preorder[1:1+leftsize]
        rightPreorder=preorder[1+leftsize:]
        lefttree=self.buildTree(leftPreorder,leftInorder)
        rightree=self.buildTree(rightPreorder,rightInorder)
        root.left=lefttree
        root.right=rightree
        return root