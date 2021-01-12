from jump_sort import jump_search

"""
Pure Python implementation of the jump search algorithm.
Examples:
>>> jump_search([0, 1, 2, 3, 4, 5], 3)
3
>>> jump_search([-5, -2, -1], -1)
2
>>> jump_search([0, 5, 10, 20], 8)
-1
>>> jump_search([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610], 55)
10
"""

print("jump_search([0, 1, 2, 3, 4, 5], 3) = {}".format(jump_search([0, 1, 2, 3, 4, 5], 3)))
print("jump_search([-5, -2, -1], -1) = {}".format(jump_search([-5, -2, -1], -1)))
print("jump_search([0, 5, 10, 20], 8) = {}".format(jump_search([0, 5, 10, 20], 8)))
print("jump_search([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610], 55) = {}".format(jump_search([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610], 55)))