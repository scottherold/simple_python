def countDown(num):
    x = num
    arr = []
    while x >= 0:
        arr.append(x)
        x = x-1
    return(arr)

def printReturn(arr):
    print(arr[0])
    return(arr[1])

def firstTotalSum(arr):
    x = arr[0]
    y = len(arr)
    return x + y

def valuesGreater(arr):
    i = 0
    x = 0
    arr2 = []
    if len(arr) <= 1:
        return False
    else:
        for element in arr:
            if arr[i] > arr[1]:
                arr2.append(arr[i])
                x = x+1
            i = i+1
        print(x)
        return arr2

def lengthAndValue(size,value):
    x = 0
    arr = []
    while x < size:
        arr.append(value)
        x = x+1
    return arr



