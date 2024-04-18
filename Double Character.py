ifRepeated = 0

givenWord = input("Please provide me with the word that you would like me to check for double characters \n")
for x in range(len(givenWord)):
    for j in range(x+1, len(givenWord)):
        if givenWord[x] ==givenWord[j]:
            ifRepeated = 1
            break


if ifRepeated == 1:
    print("sadly it repeated , im sorry")
else:
    print("This word has no repeated letters !!!")    