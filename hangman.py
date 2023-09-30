from random import choice
from words import word_list
from art import stages, logo

print(logo)
chosen_word = choice(word_list)
print(f"Solution is: {chosen_word}")
lives = 7

#Creating blanks
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    # display += "_"
    display.extend("_")

while "_" in display and lives != 0:
    guess = input("Guest a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}.")

    # Checking guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
          
    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"You guessed {guess}. That's not in the word. You lose a life.")

    print(f"{' '.join(display)}")

if lives == 0:
    print("You lose.")
else:    
    print("You win.")