# Merge UnSort List
def merge_sort(unsorted_arr):
    if len(unsorted_arr) <= 1:
        return unsorted_arr
    
    middle = len(unsorted_arr) // 2
    left_list = unsorted_arr[:middle]
    right_list = unsorted_arr[middle:]

    merge_sort(left_list)
    merge_sort(right_list)

    merge_two_sorted_list(left_list, right_list, unsorted_arr)

# Merge Two Sorted List
def merge_two_sorted_list(a,b,arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0
    

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
            k += 1
        else:
            arr[k] = b[j]
            j += 1
            k += 1
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1
   



if __name__=='__main__':

    test_cases = [

        [4,13,98,65,45,76,3,4,1,2],
        [8,0,5,34,65,4,6],
        [],
        [5],
        [76,54,34,31,5],
        [3,4,5,6]

    ]
    for i in test_cases:
        merge_sort(i)
        print(i)
