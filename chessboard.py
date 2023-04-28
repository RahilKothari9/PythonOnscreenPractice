letter = input("Enter the string")
num = int(input("Enter a number"))
mp ={"A" : 1, "B" : 2, "C" : 3}
if((mp[letter] - 1 + num - 1 ) % 2 == 0):
    print("BLACK")
else:
    print("WHITE")
