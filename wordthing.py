userword = input("Enter a word. ")

for a in range(len(userword)):
    if a % 2 == 0:
        print(userword[a].lower(), end = "")
    else:
        print(userword[a].upper(), end = "")

print(" ")
