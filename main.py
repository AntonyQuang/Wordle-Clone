import words
import random

wordlist = (words.words.split("\n"))
answer = random.choice(wordlist)

guess_list = []
for letters in range(5):
    guess_list += "✳"

guess_history = []
guess = "****"
attempts = 0

while attempts < 6 and guess_list != ["✔","✔","✔","✔","✔"]:
    attempts +=1
    while len(guess) != 5:
        guess = input(f"Attempt {attempts}/6. Guess your 5 letter word: ")
    for letter in range(5):
        if guess[letter] == answer[letter]:
            guess_list[letter] = "✔"
        elif guess[letter] in answer:
            guess_list[letter] = "✳"
        else:
            guess_list[letter] = "❌"

    guess_history.append(guess_list.copy())
    for row in guess_history:
        print(row)
        
print(f"The answer '{answer}' was correctly guessed in {attempts}/6 attempts.")
if attempts > 6:
    print(f"No more lives. The correct answer was {answer}.")
