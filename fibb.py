n = int(input("Enter a number"))
x1 = 0
x2 = 1
ls =[x1, x2]
x3 = 0
while (True):
    x3 = x1 + x2
    ls.append(x3)
    x1 = x2
    x2 = x3
    if x3 > n:
        break

if n in ls:
    print("YES")
else:
    print("NO")
