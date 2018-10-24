arr = [8,1,5,3,2,0]
# Goal : arr = [0,1,2,3,5,8]

def bubbleSort(arr):
    count = 0
    for j in range(len(arr)-1):
        # print("\n\n", "-"*100, "Iteration", j)
        for i in range(len(arr)-1-j):            
            count += 1
            #print("\n","*"*80, "\nindex ", i, "value", arr[i])
            # print("\n","*"*80, "\ncomparing", arr[i], arr[i+1])
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                # print("swapped", arr[i], arr[i+1])
                # print("array is now", arr)
            # else:
                # print("no need to swap", arr[i], arr[i+1])
    print('# of evaluations', count)
    return arr

print(bubbleSort(arr))