class Solution(object):
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        nodes = [(original, cloned)]
        while nodes:
            curr_node, curr_clone = nodes.pop(0)
            if not curr_node:
                continue
            if curr_node is target:
                return curr_clone
            nodes.append((curr_node.left, curr_clone.left))
            nodes.append((curr_node.right, curr_clone.right))