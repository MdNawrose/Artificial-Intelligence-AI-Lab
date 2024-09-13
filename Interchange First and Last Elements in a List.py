def interchange_first_last(lst):
  
    if len(lst) > 1:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

lst = input("Enter The Elements : ").split()
result = interchange_first_last(lst)

print("List After Interchange :", result)
