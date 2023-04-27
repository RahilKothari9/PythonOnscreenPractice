ls = []
x = int(input("Enter the number of numbers"))
for i in range(x):
    y = int(input("Enter the number"))
    ls.append(y)

st = set()
for i in ls:
    for j in ls:
        if (j % i == 0 and j != i):
            st.add(j)

print(st)