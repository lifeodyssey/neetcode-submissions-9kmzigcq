# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        pos = {val: i for i, val in enumerate(inorder)}  # O(1) 查 root 位置
        pre_i = 0  # 指向 preorder 当前要用的根

        def build(inL, inR):
            nonlocal pre_i
            if inL > inR:
                return None

            root_val = preorder[pre_i]
            pre_i += 1

            root = TreeNode(root_val)
            k = pos[root_val]

            root.left = build(inL, k - 1)
            root.right = build(k + 1, inR)
            return root

        return build(0, len(inorder) - 1)