from math import sqrt

def jump_search(array, target):
    i = 0
    #flag = 0
    n = len(array)
    step = int(sqrt(len(array)))
    # find the block
    while array[min(step, n)-1] < target:

        i = step
        step = step + int(sqrt(n))

        # not in array
        if step > n :
            print(step)
            #flag =1
            return None
    
    # find where is it
    while array[i] < target:
        i = i + 1

        # not in block
        if i == step:
            #flag = 2         
            return None

    if array[i] == target:
        return i
    #flag = 3
    return None