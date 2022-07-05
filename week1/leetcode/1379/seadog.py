# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        answer = cloned
    
        def symmetric(ori, clo):
            if not ori:
                return 

            # left 확인
            result = symmetric(ori.left, clo.left)
            if result:
                return result
            
            # 자신 확인
            if ori is target:
                return clo
            
            # right 확인
            result = symmetric(ori.right, clo.right)
            if result:
                return result
            

        answer = symmetric(original, cloned)
        return answer