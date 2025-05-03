import random
from hangman_words import word_list
from hangman_art import stages,logo

chosen_word = random.choice(word_list)
# print(chosen_word)

blanks=""
for i in range(len(chosen_word)):
    blanks+="_"

lives=6
right=False
print(logo)
correct_letters=[]

print(f"Word to guess: {blanks}")
while blanks!=chosen_word and lives!=0:
    guess = input("Guess a letter: ").lower()
    right = False
    if guess in correct_letters:
        print(f"You have already guessed {guess}")
        right=True
    for i,letter in enumerate(chosen_word):
        # print(f"letter and guess {letter} and {guess}")
        if letter == guess:
            right_index=i
            right=True
            correct_letters.append(guess)
            blanks=blanks[:right_index]+letter+blanks[right_index+1:]
    print(f"{blanks}")
    if not right:
        print(f"You guessed {guess}, that's not in the word. You lose a life")
        lives=lives-1
        # print(f"lives{lives}")
        print(f"Lives is now one less-->{lives}")
    print(f"*****************{lives} left ********************")
    print(stages[lives])

if lives==0:
    print("Uh OH YOU LOST")
    print(f"The word was {chosen_word}")
elif blanks==chosen_word:
    print("YOU WON!!")

