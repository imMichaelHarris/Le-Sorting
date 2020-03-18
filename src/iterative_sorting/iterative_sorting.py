# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc) 
        # Loop through the rest of array and keep track of the 
        # array and when the index is smaller than the smallest index variable
        # swap the values
        for j in range(cur_index + 1, len(arr) ):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        

        # TO-DO: swap
        old = arr[cur_index]
        arr[cur_index] = arr[smallest_index]
        arr[smallest_index] = old
        print(arr)


    return arr

# selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])

# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    # Get the first element and compare with the next element
    # Have a swap tracker and every loop if you swap go through the process again
    # IF no swaps its sorted
    sorting = True
    while sorting:
        swaps = 0
        for i in range(0, len(arr) -1):
            og = arr[i]
            if arr[i+1] < arr[i]:
                arr[i] = arr[i+1]
                arr[i + 1] = og
                swaps += 1

        if swaps == 0:
            sorting = False

    return arr

print(bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))

# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr