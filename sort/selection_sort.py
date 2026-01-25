def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        temp = my_list[i]
        my_list[i] = my_list[min_index]
        my_list[min_index] = temp
    return my_list

#0 1 2 3 4 5
#4 2 6 5 1 3

#min = 4
#j = 2
#j < min min = j = 2
#1 2 6 5 4 3
#i = 6
#j = 5
#min = 6
#j < 6
#min = 5
#min = 3
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
