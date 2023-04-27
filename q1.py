
txt = input("Enter your string")
def func(s):
    vow = 0
    con = 0
    for letter in s:
        if(letter in 'aeiouAEIOU'):
            vow += 1
        elif (letter != ' '):
            con += 1
    return [vow, con]
ls = func(txt)
print("consonants", ls[1],  "vow", ls[0])