
li=[12,10,18,98,17,19,32,99,67,32]
largest = li[0]
smallest=li[0]

for i in li:
    if i > largest:
        largest = i
    elif i<smallest:
        smallest=i

print(f"The largest number is:{largest}")
print(f"The smallest number is :{smallest}")