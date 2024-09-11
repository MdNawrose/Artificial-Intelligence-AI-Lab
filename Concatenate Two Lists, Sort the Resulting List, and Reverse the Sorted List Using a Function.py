ef process_lists(list1, list2):

    concatenated_list = list1 + list2
    sorted_list = sorted(concatenated_list)
    reversed_sorted_list = sorted_list[::-1]

    return reversed_sorted_list


list1 = [8,6,7,5]
list2 = [3,1,4,2]

result = process_lists(list1, list2)
print("Reversed sorted list:", result)
