x = int(input("Enter your number: "))

copy = x
res = 0
while(x != 0):
    res *= 10
    res += (x % 10)
    x //= 10

print(res)