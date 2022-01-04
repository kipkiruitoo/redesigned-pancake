# import helper functions from jovian
from jovian.pythondsa import evaluate_test_cases


# ======================Question===================================
#  Alice has some cards with numbers written on them. 
#  She arranges the cards in decreasing order,
#  and lays them out face down in a sequence on a table. 
#  She challenges Bob to pick out the card containing a given 
#  number by turning over as few cards as possible. 
#  Write a function to help Bob locate the card.



# Come up with all possible scenarios and example inputs and outputs


# example input
test = {
    'input': { 
        'cards': [13, 11, 10, 7, 4, 3, 1, 0], 
        'query': 7
    },
    'output': 3
}

# We can store then in a List of Dictionaries to make it easier
tests = []


#1. Query occurs in the middle
tests.append(test)

tests.append({
    'input': {
        'cards': [13, 12, 10, 8, 5, 3, 1, 0],
        'query': 1
    },
    'output': 6
})


#2. Query is the last element
tests.append({
    'input': {
        'cards': [3, -1, -9, -127],
        'query': -127
    },
    'output': 3
})



#3. Cards contains just one element, query
tests.append({
    'input': {
        'cards': [4],
        'query': 4
    },
    'output': 0 
})

#4. Cards does not contain query . return -1 if not contained
tests.append({
    'input': {
        'cards': [9, 7, 5, 1, -3],
        'query': 4
    },
    'output': -1
})


#5. Cards is empty return -1
tests.append({
    'input': {
        'cards': [],
        'query': 7
    },
    'output': -1
})


#6. numbers can repeat in cards.
# should return the first occurence although any 
# position of the query will still be a valid output
tests.append({
    'input': {
        'cards': [8, 7, 6, 6, 6, 5, 5, 3, 2, 2, 1, 1, 0, 0],
        'query': 3
    },
    'output': 7
})


tests.append({
    'input': {
        'cards': [9, 9, 6, 6, 6, 5, 5, 5, 3, 2, 1, 1, 0, 0, 0],
        'query': 6
    },
    'output': 2
})




# Solution 1 - Brute force.
# simply iterate through the number checking if its the number you are looking for.
# this is called Linear search Algorithm


def locate_card(cards, query):

    # create a variable position to hold our poition as we traverse through the cards.
    position = 0

# create a while loop to go through each card one by one
    while position != len(cards):
        # if the position is equals the query, return the position
        if cards[position] == query:
            return position
        
        # else add 1 to the position to go to the next position and check again
        position +=1


# if the loop finishes and we didn't find the position, return -1
    return -1


# Lets now test our solution with our first input. Should hopefully work using jovian's evaluate test_cases
# result = locate_card(test['input']['cards'], test['input']['query'])
# # print(result)


# # should be true if our brute force worked
# # print(result == test['output'])

print(tests)
# evaluate_test_cases(locate_card, tests)

# ==================Output===========================

# ←[1mTEST CASE #0←[0m

# Input:
# {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}

# Expected Output:
# 3


# Actual Output:
# 3

# Execution Time:
# 0.014 ms

# Test Result:
# ←[92mPASSED←[0m


# ←[1mTEST CASE #1←[0m

# Input:
# {'cards': [13, 12, 10, 8, 5, 3, 1, 0], 'query': 1}

# Expected Output:
# 6


# Actual Output:
# 6

# Execution Time:
# 0.021 ms

# Test Result:
# ←[92mPASSED←[0m


# ←[1mTEST CASE #2←[0m

# Input:
# {'cards': [3, -1, -9, -127], 'query': -127}

# Expected Output:
# 3


# Actual Output:
# 3

# Execution Time:
# 0.013 ms

# Test Result:
# ←[92mPASSED←[0m


# ←[1mTEST CASE #3←[0m

# Input:
# {'cards': [4], 'query': 4}

# Expected Output:
# 0


# Actual Output:
# 0

# Execution Time:
# 0.015 ms

# Test Result:
# ←[92mPASSED←[0m


# ←[1mTEST CASE #4←[0m

# Input:
# {'cards': [9, 7, 5, 1, -3], 'query': 4}

# Expected Output:
# -1


# Actual Output:
# -1

# Execution Time:
# 0.013 ms

# Test Result:
# ←[92mPASSED←[0m


# ←[1mTEST CASE #5←[0m

# Input:
# {'cards': [], 'query': 7}

# Expected Output:
# -1


# the solution works. We should now try a better solution.
#  This problem is best solved using a binary search algorithm to ensure minimal flipping of cards.
# Linear search often has a complexity of O(N) and a space complexity of O(1).


# Here's how binary search can be applied to our problem:

#1. Find the middle element of the list.
#2. If it matches queried number, return the middle position as the answer.
#3. If it is less than the queried number, then search the first half of the list
#4. If it is greater than the queried number, then search the second half of the list
#5. If no more elements remain, return -1.

def locate_card_using_binary_search(cards, query):
    lo, hi = 0, len(cards) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]

        print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)

        if mid_number == query:
            return mid
        if mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid + 1

    return -1


evaluate_test_cases(locate_card_using_binary_search, tests)


#  our final algorithm has the time complexity O(log N). This fact is often stated as: binary search runs in logarithmic time.
#  You can verify that the space complexity of binary search is O(1).