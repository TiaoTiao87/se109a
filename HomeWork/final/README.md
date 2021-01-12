# [Jump Search Algorithm](https://www.studytonight.com/data-structures/jump-search-algorithm)
## Algorithm of Jump Search
Input :
1. Sorted array A of size n
2. Element(x) to be searched

Output :

A valid location of x in the array A
Steps :
1. Set i=0 and step = √n.

2. Compare A[i] with item. If A[i] != x and A[i] < x, then jump to the next block. 
Also, do the following:
    1. Set i = step
    2. Increment step by √n
3. Repeat the step 2 till step < n-1
4. If A[i] > x, then move to the beginning of the current block and perform a linear search.

    1. Set p = i
    2. Compare A[p] with item. If A[p]== item, then print p as the valid location else set p++
    3. Repeat Step 4.1 and 4.2 till p < step
5. Exit
## 撰寫程式
```
from math import sqrt

def jump_search(array, target):
    i = 0
    n = len(array)
    step = int(sqrt(len(array)))

    # find the block
    while array[min(step, n)-1] < target:
        i = step
        step = step + int(sqrt(n))

        # not in array
        if step > n - 1:
            return None
    
    # find where is it
    while array[i] < target:
        i = i + 1

        # not in block
        if i == step:
            return None
    if array[i] == target:
        return i
    return None
```
## 撰寫測試程式
```
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
```
## 測試結果
```
PS D:\se109a\HomeWork\final> python.exe .\jump_sort_test.py
jump_search([0, 1, 2, 3, 4, 5], 3) = 3
jump_search([-5, -2, -1], -1) = None
jump_search([0, 5, 10, 20], 8) = None
jump_search([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610], 55) = 10
```
jump_search([-5, -2, -1], -1) = None
此行出錯，發現是
```
# not in array
if step > n -1:
    print(step)
    #flag =1
    return None
```
出錯，修改成
```
# not in array
if step > n :
    print(step)
    #flag =1
    return None
```
第二次測試
```
PS D:\se109a\HomeWork\final> python .\jump_sort_test.py
jump_search([-5, -2, -1], -1) = 2
jump_search([0, 1, 2, 3, 4, 5], 3) = 3
jump_search([-5, -2, -1], -1) = 2
jump_search([0, 5, 10, 20], 8) = None
jump_search([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610], 55) = 10
```
成功!
## 時間複雜度
此函釋的時間複雜度為 o(√n)，因為
```
while array[min(step, n)-1] < target:
        i = step
        step = step + int(sqrt(n))

        # not in array
        if step > n - 1:
            return None
```