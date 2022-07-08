# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        # 1. quadTree1 = leaf node, quadTree2 = leaf node
        if quadTree1.isLeaf and quadTree2.isLeaf:
            node = Node(quadTree1.val | quadTree2.val, 1, None, None, None, None)
            return node
        # 2. quadTree1 = leaf node, quadTree2 = NOT leaf node
        elif quadTree1.isLeaf and not quadTree2.isLeaf:
            node = Node(0, 0,
                       self.intersect(quadTree1, quadTree2.topLeft),
                       self.intersect(quadTree1, quadTree2.topRight),
                       self.intersect(quadTree1, quadTree2.bottomLeft),
                       self.intersect(quadTree1, quadTree2.bottomRight))
        # 3. quadTree1 = NOT leaf node, quadTree2 = leaf node
        elif not quadTree1.isLeaf and quadTree2.isLeaf:
            node = Node(0, 0,
                       self.intersect(quadTree1.topLeft, quadTree2),
                       self.intersect(quadTree1.topRight, quadTree2),
                       self.intersect(quadTree1.bottomLeft, quadTree2),
                       self.intersect(quadTree1.bottomRight, quadTree2))
        # 4. quadTree1 = NOT leaf node, quadTree2 = NOT leaf node
        else:
            node = Node(0, 0,
                       self.intersect(quadTree1.topLeft, quadTree2.topLeft),
                       self.intersect(quadTree1.topRight, quadTree2.topRight),
                       self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft),
                       self.intersect(quadTree1.bottomRight, quadTree2.bottomRight))
        
        # 만약 모두 다 같다면, 그냥 한가지만 사용
        if node.topLeft.isLeaf and node.topRight.isLeaf and node.bottomLeft.isLeaf and node.bottomRight.isLeaf and node.topLeft.val == node.topRight.val == node.bottomLeft.val == node.bottomRight.val:
            return Node(node.topLeft.val, 1, None, None, None, None)
        return node