




# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    # These arrays will be sorted already 
    # Compare the beginning of each already and whichever is smaller set it in merege_arr
    # Keep track of which element in array you are on
    # When choosing an element to put in merged_arr increment the index of the array pulled from
    sorting = True
    arrA_index = 0
    arrB_index = 0
    merged_arr_index = 0
    print(f"A- {arrA_index}, B - {arrB_index}")
    print(arrA, arrB)
    while sorting:
        if arrA[arrA_index] <= arrB[arrB_index]:
            merged_arr[merged_arr_index] = arrA[arrA_index]
            merged_arr_index += 1
            arrA_index += 1
        elif arrA[arrA_index] > arrB[arrB_index]:
            merged_arr[merged_arr_index] = arrB[arrB_index]
            merged_arr_index += 1
            arrB_index += 1

    print(merged_arr)
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    if len(arr) <= 1:
        return arr

    half = len(arr) // 2
    left = arr[ :half]
    right = arr[half:]

    return merge(merge_sort(left), merge_sort(right))

print(merge_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
