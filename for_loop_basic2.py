def makeItBig(arr):
    i = 0
    for element in arr:
        if arr[i] > 0:
            arr[i] = "big"
        i = i+1
    return arr

def countPositives(arr):
    i = 0
    x = 0
    for element in arr:
        if arr[i] > 0:
            x = x+1
        i = i+1
    arr[i-1] = x
    return arr

def sumTotal(arr):
    i = 0
    x = 0
    for element in arr:
        x = x + arr[i]
        i = i + 1
    return x

def multiples(arr):
    i = 0
    x = 0
    for element in arr:
        x = x + arr[i]
        i = i + 1
    mult = x / len(arr)
    return mult

def length(arr):
    x = len(arr)
    return x

def minimum(arr):
    i = 0
    x = arr[0]
    if len(arr) <= 0:
        return False
    else:
        for element in arr:
            if arr[i] < x:
                x = arr[i]
            i = i + 1
    return x

def maximum(arr):
    i = 0
    x = arr[0]
    if len(arr) <= 0:
        return False
    else:
        for element in arr:
            if arr[i] > x:
                x = arr[i]
            i = i + 1
    return x

def ultimateAnalyze(arr):
    i = 0
    sumTotal = 0
    minimum = arr[0]
    maximum = arr[0]
    for element in arr:
        if arr[i] > maximum:
            maximum = arr[i]
        if arr[i] < minimum:
            minimum = arr[i]
        sumTotal = sumTotal + arr[i]
        i = i + 1
    my_dictionary = {"sumTotal":sumTotal,"average":sumTotal / len(arr),"minimum":minimum,"maximum":maximum,"arrLength":len(arr)}
    return my_dictionary

def reverseList(arr):
    i = 0
    x = len(arr)-1
    for element in arr:
        if x > i:
            y = arr[i]
            arr[i] = arr[x]
            arr[x] = y
        i = i + 1
        x = x - 1
    return arr

