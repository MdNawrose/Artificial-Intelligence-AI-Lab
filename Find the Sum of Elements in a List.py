def sum_of_elements(lst):

    return sum(lst)
  
lst = list(map(int, input("Enter The Elements: ").split()))
result = sum_of_elements(lst)

print(f"The Sum Of The Elements : {result}")
