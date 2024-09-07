def count_occurrences(lst, element):
    count = 0

    for item in lst:
        if item == element:
            count += 1
    return count

lst = input("Enter the elements of the list separated by spaces: ").split()
element = input("Enter the element to count: ")

result = count_occurrences(lst, element)

print(f"The element '{element}' occurs {result} time(s) in the list.")

