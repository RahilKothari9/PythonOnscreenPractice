x = int(input("Enter the number of words"))
ls = []
for i in range(x):
    s = input("Enter your word")
    ls.append(s)

max_size = 0
for element in ls:
    if(len(element) > max_size):
        max_size = len(element)

print(max_size)