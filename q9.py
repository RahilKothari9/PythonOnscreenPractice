s = input("Enter a string")
d1 = {}
for i in s:
    if i in d1:
        d1[i] += 1
    else:
        d1[i] = 1
print(d1)