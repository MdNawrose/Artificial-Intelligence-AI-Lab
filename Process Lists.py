def process_lists(list1, list2):
 
    concatenated_list = list1 + list2
    sorted_list = sorted(concatenated_list)
    reversed_sorted_list = sorted_list[::-1]

    return reversed_sorted_list


list1 = [1,2,3,4]
list2 = [5,6,7,8]

result = process_lists(list1, list2)
print("Reversed sorted list:", result)
