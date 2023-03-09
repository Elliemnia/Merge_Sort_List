# Merge UnSort List
def merge_sort(unsorted_arr):
    if len(unsorted_arr) <= 1:
        return unsorted_arr
    middle = len(unsorted_arr) // 2
    left_list = unsorted_arr[:middle]
    right_list = unsorted_arr[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    return merge_two_sorted_list(left_list,right_list)

# Merge Two Sorted List
def merge_two_sorted_list(a,b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = 0
    j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1
    while i < len_a:
        sorted_list.append(a[i])
        i += 1
    while j < len_b:
        sorted_list.append(b[j])
        j += 1
    return sorted_list



if __name__=='__main__':
    llist = [4,13,98,65,45,76,3,4,1,2]
    print(merge_sort(llist))
