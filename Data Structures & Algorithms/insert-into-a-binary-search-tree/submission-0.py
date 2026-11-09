# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: #Base case
            return TreeNode(val)

        if val > root.val: #If it belongs right of the node
            root.right = self.insertIntoBST(root.right, val)
        elif val < root.val : #If it belongs on the left
            root.left = self.insertIntoBST(root.left, val)

        return root #return og root with its changes