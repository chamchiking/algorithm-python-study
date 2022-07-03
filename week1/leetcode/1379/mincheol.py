# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
global answer


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        dfs(original, cloned, target)

        return answer


def dfs(current, clone, target):
    global answer
    if current.left:
        dfs(current.left, clone.left, target)
    if current == target:
        answer = clone
    if current.right:
        dfs(current.right, clone.right, target)
