import random
print("Hangman Python")

filename = "wordlist.txt"
wordliststorage = open(filename, 'r')
wordlist = wordliststorage.read()

SecretWord = random.choice(wordlist.split())
print(SecretWord)
fails = 0
loop = True
CorrectLetters = ""


while loop:
    #print(CorrectLetters)
    letter = input("Enter a letter: ")
    if letter == "quit":
        loop = False

    if letter in SecretWord:
        print("Correct!")
        for letterindex in range(0, len(SecretWord)):
            for correctlettersindex in range(0, len(CorrectLetters)):
                if CorrectLetters[correctlettersindex] == SecretWord[letterindex]:
                    print(CorrectLetters[correctlettersindex], end = "")
            if letter in SecretWord[letterindex]:
                print(letter, end = "")
                CorrectLetters = CorrectLetters + letter
            else:
                print("_ ", end = "")
            print(" ")
    else:
        print("Sorry, Try Again.")
        fails + 1
    if CorrectLetters in SecretWord:
        print("You win!")
