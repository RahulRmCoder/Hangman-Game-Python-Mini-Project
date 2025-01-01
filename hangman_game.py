import random
from hangman_words import word_list
from hangman_art import stages, logo

play_again=True
while play_again:

    lives = 6

    print(logo)

    chosen_word = random.choice(word_list)

    placeholder = ""
    word_length = len(chosen_word)
    for position in range(word_length):
        placeholder += "_"
    print("Word to guess: " + placeholder)

    game_over = False
    correct_letters = []

    while not game_over:

        print(f"****************************{lives}/6 LIVES LEFT****************************")

        guess = input("Guess a letter: ").lower()

        if guess in correct_letters:
            print(f'You have already guessed {guess}')
        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
                correct_letters.append(guess)
            elif letter in correct_letters:
                display += letter
            else:
                display += "_"

        print("Word to guess: " + display)

        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed {guess}, that's not in the word. You lost a life")
            if lives == 0:
                game_over = True

                print(f"\n***********************IT WAS {chosen_word}! YOU LOSE**********************")

        if "_" not in display:
            game_over = True
            print("\n****************************YOU WIN****************************")

        print(stages[lives])

    play=input("Do you want to play again(Y/N):").lower()
    if play=='y':
        print("\nThank You 😊. Then lets start the game again")
    else:
        play_again=False
        print("\nSure!, Thank You for playing this game 🙏")

