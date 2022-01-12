# Here's a function to count the number of nodes in a binary tree.

def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)
