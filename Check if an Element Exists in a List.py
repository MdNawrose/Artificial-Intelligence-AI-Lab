def check_element_exists(lst, element):

    return element in lst

lst = input("Enter The Elements : ").split()

element = input("Enter The Element To Check: ")

if check_element_exists(lst, element):
    print(f"The Element '{element}' Exists In The List.")
else:
    print(f"The Element '{element}' Does Not Exist In The List.")
