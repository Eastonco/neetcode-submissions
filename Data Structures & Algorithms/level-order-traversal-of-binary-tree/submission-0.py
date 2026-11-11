# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = []
        res = []
        if not root:
            return []
        q.append(root)

        while q:
            toPop = len(q)
            level = []
            for i in range(toPop):
                tmp = q.pop(0)
                level.append(tmp.val)
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)
            res.append(level)
        
        return res
                

        