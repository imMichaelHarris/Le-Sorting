




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
    
    subA = 0
    subB = 0
    for i in range(elements):
        print("if", i, arrA, arrB)
        if len(arrA) == subA:
             merged_arr[i] = arrB[subB]
             subB += 1
        elif len(arrB) == subB:
             merged_arr[i] = arrA[subA]
             subA += 1
        elif arrA[subA] >= arrB[subB]:
            print(f"if statement")
            merged_arr[i] = arrB[subB]
            subB += 1
        elif arrB[subB] >= arrA[subA]:
            # print(f"elif {subB}, {subA}")
            merged_arr[i] = arrA[subA]
            subA += 1
            print(f"2nd elif {subB}, {subA}")

            
        else:
            print("no", arrA[0], arrB[0])
    # while sorting:
    #     print("pppp")
    #     print("now")
    #     print(f"A- {arrA_index}, B - {arrB_index}")
    #     print(arrA, arrB, merged_arr)
    #     if arrA_index == len(arrA):
    #         print("here")
    #         merged_arr[merged_arr_index] = arrB[arrB_index]
    #         merged_arr_index += 1
    #         arrB_index += 1
    #     elif arrB_index == len(arrB):
    #         print("hi")
    #         merged_arr[merged_arr_index] = arrA[arrA_index]
    #         merged_arr_index += 1
    #         arrA_index += 1
    #     elif arrA[arrA_index] <= arrB[arrB_index]:
    #         merged_arr[merged_arr_index] = arrA[arrA_index]
    #         merged_arr_index += 1
    #         arrA_index += 1
    #         print("boo")
    #     elif arrA[arrA_index] > arrB[arrB_index]:
    #         merged_arr[merged_arr_index] = arrB[arrB_index]
    #         merged_arr_index += 1
    #         arrB_index += 1
    #     else:
    #         sorting = False


    print(merged_arr)
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

    if len(arr) <= 1:
        return arr

    half = int(len(arr) / 2)
    leftArr = arr[ :half]
    rightArr = arr[half:]

    left = merge_sort(leftArr)
    right = merge_sort(rightArr)
    return merge(left, right)

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
