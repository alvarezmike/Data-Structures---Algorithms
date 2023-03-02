def bubble_sort(my_list):
    for i in range(len(my_list) - 1 , 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list

print(bubble_sort([4, 3, 7, 6,2, 1]))

# in bubble sort you compare the first value to the second one and
# rearranges based on order of values
# and keep looping until the list is in ascending order