
# The height/depth of a binary tree is defined as the length of the longest path from its root node to a leaf. It can be computed recursively, as follows:

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))
