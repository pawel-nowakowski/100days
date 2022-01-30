from random import choice
import hangman_words
import hangman_art
# word list
word_list = hangman_words.word_list

# pick a random word
picked_word = choice(word_list)
masked_word = list(len(picked_word) * '_')

life = 6

stages = hangman_art.stages
logo = hangman_art.logo

print(logo)
while '_' in masked_word:
    print(stages[life])
    print(''.join(masked_word))
    print('\n')
    letter = input("Guess a letter: ").lower()
    if letter in masked_word:
        print("You already used this letter.")
    elif letter in picked_word:
        for i in range(len(picked_word)):
            if letter == picked_word[i]:
                masked_word[i] = letter
        print("Your guess was right.")
    else:
        print('Your guess was wrong.')
        life -= 1
        if life == 0:
            break

if life != 0 or '_' not in masked_word:
    print(f"You guessed the whole word: {picked_word}!")
else:
    print("You lost.")