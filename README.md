# Hangman Game

Welcome to the **Hangman Game**! This is a Python-based implementation of the classic word-guessing game. Test your vocabulary and deduction skills while having fun!

## How to Play

The objective of the game is to guess the hidden word by guessing one letter at a time. You have a total of 6 lives. Each incorrect guess costs you a life. If you lose all your lives before guessing the word, you lose the game. If you successfully guess all the letters, you win!

### Features
- Randomly selects a word from a predefined list.
- Tracks guessed letters to prevent duplicate guesses.
- Displays the word progress after each guess.
- ASCII art stages for visual feedback.
- Option to play again after the game ends.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/RahulRmCoder/Hangman-Game-Python-Mini-Project.git
   ```

2. Navigate to the project directory:
   ```bash
   cd hangman-game
   ```

3. Ensure you have Python installed (version 3.6 or later).

4. Install any required dependencies (if any).

5. Run the game:
   ```bash
   python hangman.py
   ```

## Files Included

- `hangman.py`: The main script to run the game.
- `hangman_words.py`: Contains a list of words used in the game.
- `hangman_art.py`: Contains the ASCII art stages and logo for the game.

## How to Customize

1. Add more words to the `word_list` in `hangman_words.py` to expand the game's vocabulary.
2. Customize the ASCII art in `hangman_art.py` to create your own stages or logos.

## Example Gameplay

```
****************************6/6 LIVES LEFT****************************
Word to guess: _ _ _ _
Guess a letter: e
Word to guess: _ e _ _

****************************5/6 LIVES LEFT****************************
Word to guess: _ e _ _
Guess a letter: a
You guessed a, that's not in the word. You lost a life.
```

## Acknowledgments

- Inspired by the classic Hangman game.
- ASCII art provided by the developers.

## Contributing

Feel free to fork this repository and submit pull requests for improvements or new features. Contributions are welcome!

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or suggestions, please contact:
- Rahul Rajasekharan Menon: [rahulrajasekharanmenon64325@gmail.com]
- GitHub: [https://github.com/RahulRmCoder](https://github.com/RahulRmCoder)

Enjoy the game!


