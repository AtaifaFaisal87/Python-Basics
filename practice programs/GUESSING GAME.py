print("------------------------------------")
print("           GUESS THE NUMBER         ")
print("------------------------------------")

num = 9
i = 1

while i <= 3:
    n = int(input("GUESS: "))

    if n == num:
        print("YOU HAVE GUESSED IT CORRECT")
        break
    else:
        print("WRONG GUESS")

    i += 1

if i > 3:
    print("FAILED!")