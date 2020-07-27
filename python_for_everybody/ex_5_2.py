largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        n = int(num)
    except:
        print("Invalid input")
        continue
    if smallest == None:
        smallest = n
    if largest == None:
        largest = n
    if n < smallest:
        smallest = n
    if n > largest:
        largest = n

print("Maximum is", largest)
print("Minimum is", smallest)