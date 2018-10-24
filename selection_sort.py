arr = [8,5,2,6,9,3,1,4,0,7]

def selection_sort(arr):
    for j in range(len(arr)):
        x = j
        for i in range(j,len(arr)):
            if arr[i] < arr[x]:
                x = i
        arr[x], arr[j] = arr[j], arr[x]
    return arr

print(selection_sort(arr))
