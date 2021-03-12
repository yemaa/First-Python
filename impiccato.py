import random

with open ("impiccato1.txt", "r") as f:
    words = f.readlines()

word = random.choice(words)[:-1]

allowedErrors = 8
guesses = []
done = False 

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")
    done = True

    guess = input(f"Allowed Errors Left: {allowedErrors}. Next guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowedErrors -= 1
        if allowedErrors == 0:
            break

    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False


if done:
    print(f"You found the word! It was '{word}'!")
else:
    print(f"Game over! The word was '{word}'")

