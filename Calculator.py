a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
ch=input("Enter the operation you want to perform")

if ch=='+':
    print(a+b)
elif ch=='-':
    print(a-b)
elif ch=='/':
    print(a/b)
elif ch=='*':
    print(a*b)
else:
    print("Incorrect input")