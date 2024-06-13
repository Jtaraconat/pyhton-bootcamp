#HANGMAN PROJECT
import random
import hangman_art
import hangman_words

word_list = hangman_words.word_list
stages = hangman_art.stages
logo = hangman_art.logo
lives = 6
guessed_letter = []

#TODO1 choose a random word and assign to chosen_word
#TODO1 create empty list display, for each letter of chosen_word display a "_"
#TODO1 use while loop to let user guiess again, loop stop when display have no "_" and all letters in chosen_word are guessed
chosen_word = random.choice(word_list)


word_length = len(chosen_word)
display = []
for n in range(word_length):
   display.append("_")



#TODO2 ask the user to guess a letter, assign answer to guess, guess is lowercase
#TODO2 loop through chosen word and replace letter in display if true
#TODO2 if guess is not a letter in chosen_word, reduce live by 1, if lives = 0 game over 
end_of_game = False

print(logo)
while not end_of_game:
    guess = input("Guess a letter: ").lower()


#TODO3 check if guess is one of the letter of chosen_word

    if guess in display:
       print(f"You've already guessed {guess}") 

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word, you lose a life")
        lives -= 1     
        if lives == 0:
            print(f"{' '.join(display)}")
            end_of_game = True
            print(f"You lose, the solution was {chosen_word}")
        
    print(f"{' '.join(display)}")
    print(stages[lives])

    if "_" not in display and lives >= 1 :
        print(f"{' '.join(display)}")
        end_of_game = True
        print("You won!!")


