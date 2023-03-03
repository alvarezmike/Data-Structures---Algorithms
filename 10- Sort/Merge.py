def merge(list1,list2):
    """Merge sort function: takes two list and puts them together in ascending order"""
    combined = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            combined.append(list1[i])
            i+=1
        else:

            combined.append(list2[j])
            j += 1

    while i < len(list1):
        combined.append(list1[i])
        i += 1

    while j < len(list2):
         combined.append(list2[j])
         j += 1

    return combined

# testing method
# print(merge([1,2,7,8], [3,4,5,6]))

def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid_index = int(len(my_list) / 2)
    left = merge_sort(my_list[:mid_index])
    right = merge_sort(my_list[mid_index:])

    return merge(left, right)


# testing method
original_list = [3,1,4,2]
sorted_list = merge_sort(original_list)

print("Original list:" , original_list)

print("Sorted list:" , sorted_list)