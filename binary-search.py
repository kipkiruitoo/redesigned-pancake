# General Strategy for Binary Search
# Here is the general strategy behind binary search, which is applicable to a variety of problems:

#1. Come up with a condition to determine whether the answer lies before, after or at a given position
#2. Retrieve the midpoint and the middle element of the list.
#3. If it is the answer, return the middle position as the answer.
#4. If answer lies before it, repeat the search with the first half of the list
#5. If the answer lies after it, repeat the search with the second half of the list.

# https://jovian.ai/kipkiruitoo/python-binary-search-assignment

def binary_search(lo, hi, condition):
    """TODO - add docs"""
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1