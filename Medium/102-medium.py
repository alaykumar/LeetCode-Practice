# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # create arr for final ans
        levels = []

        # if there it no root, return the levels arr
        if not root:
            return levels

        # helper function to append values to ans arr (levels)
        def helper(node, level):

            # if the len of ans arr and level counter is same, add new empty arr to the ans arr
            if len(levels) == level:
                levels.append([])
            
            # append the current node value inside the newly added sub arr
            levels[level].append(node.val)

            # if node exists on left, pass it to helper funtion and increase level by 1 for next level
            if node.left:
                helper(node.left, level+1)
            # if node exists on left, pass it to helper funtion and increase level by 1 for next level
            if node.right:
                helper(node.right, level+1)

        # initial index of the ans arr has to be the root of the tree with level 0
        helper(root, 0)

        # return the final ans arr
        return levels
        
        
        
        
        