# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        #Base Case If no node of key exists, return nothing
        if not root:
            return None

        if (key > root.val): #Key could be to the right
            root.right = self.deleteNode(root.right, key)
        elif (key < root.val): #Key could be to the right
            root.left = self.deleteNode(root.left, key)
        else: #Key is found
            
            if not root.left: #No left children
                return root.right
            
            if not root.right: #No right children
                return root.left
            #the key node has 2 children

            curr = root.right
            while curr.left:
                curr = curr.left #finding min value in right subtree

            root.val = curr.val #setting root value to the inorder successor

            root.right = self.deleteNode(root.right, curr.val)


        return root
        