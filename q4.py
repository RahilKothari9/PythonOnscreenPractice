def factsimple(n):
    sum = 1
    for i in range(1, n + 1):
        sum *= i
    return sum

def factrecursion(n):
    if n == 1:
        return 1
    else:
        return n * factrecursion(n - 1)
    
print(factsimple(5))
print(factrecursion(5))