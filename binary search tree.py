class BSTNode():
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


# QUESTION 8: Write a function to check if a binary tree is a binary search tree(BST).

# QUESTION 9: Write a function to find the maximum key in a binary tree.

# QUESTION 10: Write a function to find the minimum key in a binary tree.


# Here's a function that covers all of the above:
#

def remove_none(nums):
    return [x for x in nums if x is not None]


def is_bst(node):
    # if the node is None, it means that our tree is balanced but with no children
    if node is None:
        return True, None, None

   # we recusrively check if the right subtree and right subtree is a bst and get the max  and min key
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)


# check if the left subtree is a bst and the right subtree is a bst.

    is_bst_node = (is_bst_l and is_bst_r and

                   # also check if the max key in the left subtree is None or current key is greater than max_l
                   (max_l is None or node.key > max_l) and
                   #    also check if the max key in the left subtree is None or current key is greater than max_l
                   (min_r is None or node.key < min_r))

    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))

    # print(node.key, min_key, max_key, is_bst_node)

    return is_bst_node, min_key, max_key

    # inserting into a bst


def insert(node, key, value):
    if node is None:
        node = BSTNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node

    return node


# QUESTION 11: Find the value associated with a given key in a BST.


def find(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return find(node.left, key)
    if key > node.key:
        return find(node.right, key)


# QUESTION 12: Write a function to update the value associated with a given key within a BST

def update(node, key, value):
    target = find(node, key)
    if target is not None:
        target.value = value


# QUESTION 13: Write a function to retrieve all the key-values pairs stored in a BST in the sorted order of keys.
def list_all(node):
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)


# QUESTION 14: Write a function to determine if a binary tree is balanced.

def is_balanced(node):
    if node is None:
        return True, 0
    balanced_l, height_l = is_balanced(node.left)
    balanced_r, height_r = is_balanced(node.right)
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
    height = 1 + max(height_l, height_r)
    return balanced, height

# QUESTION 15: Write a function to create a balanced BST from a sorted list/array of key-value pairs.


def make_balanced_bst(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return None

    mid = (lo + hi) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = make_balanced_bst(data, lo, mid-1, root)
    root.right = make_balanced_bst(data, mid+1, hi, root)

    return root
