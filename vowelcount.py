word=input("Enter the word")
v=["a","e","i","o","u","A","E","I","O","U"]
count=0
for i in word:
    if i in v:
        count+=1

print(count)