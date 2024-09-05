
   1st Lab Assignment Q8
    def second_largest(lst):
   
    a = list(set(lst))
    
    if len(a) < 2:
        return None
    
    a.sort(reverse=True)
  
    return a[1]

lst = list(map(int, input("Enter The Elements: ").split()))

result = second_largest(lst)

if result is None:
    print("Does Not Have A Second Largest Element.")
else:
    print(f"The Second Largest Number Is: {result}")

