ls = []
x = int(input("Enter the number of numbers"))
for i in range(x):
    y = int(input("Enter the number"))
    ls.append(y)


lseven = list(filter(lambda x: x % 2 == 0, ls))
lsodd = list(filter(lambda x: x % 2 != 0, ls))

print(lseven)
print(lsodd)