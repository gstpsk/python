import os

print("""
     An Animal And His Owner
            by gstpsk



     Thank you for playing.
        © 2018 gstpsk.


""")
input()
os.system('clear')

adjective1 = input("Enter an adjective.")
animal1 = input("Enter an animal.")
adjective2 = input("Enter an adjective.")
name1 = input("Enter a name.")
adjective3 = input("Enter an adjective.")
adjective4 = input("Enter an adjective.")
adjective5 = input("Enter an adjective.")
verb1 = input("Enter a verb ending with ed.")
verb2 = input("Enter a verb ending with ed.")
noun1 = input("Enter a noun.")
verb3 = input("Enter a verb.")
famousname1 = input("Enter a name of a famous person.")

os.system('clear')

#sentence1
print("Once, there was a/an", adjective1, animal1, "and his", adjective2, "owner,", name1,)

#sentence2
print("The owner", name1, "thought his", animal1, "was very", adjective3)

#sentence3
print("The", animal1, "disagreed.")

#sentence4
print("The", animal1, "thought he was very", adjective4, "and", adjective5)

#sentence5
print("The", animal1, verb1, "the owner; the owner had no idea the", animal1, "could speak!")

#sentence6
print("The owner", verb2, "out of his", noun1, "in amazement!")

#sentence6
print('"Yeah, I can', verb3, ',"', 'said the monkey-duck.')

#sentence7
print('"Yeah", said the owner.')

#sentence8
print('"You', verb3, 'just like', famousname1, '!"')
