word = raw_input("Enter a word for the player to guess: ")
for i in range(20):
    print("\n")


def hangman(word):
    incorrect_guesses = []
    wrong = 0
    stages = ["", "_______       ", "|             ", "|      |       ", "|      O       ",\
    "|     /|\     ", "|     / \     ", "|             "]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print ("Welcome to Hangman")
    print ("Don't cheat and scroll up!")

    while wrong < len(stages) - 1:
        print ("\n")
        print (" ".join(board))
        message_to_player = "Guess a letter: "
        character = raw_input(message_to_player)
        if character in rletters:
            cind = rletters.index(character)
            board[cind] = character
            rletters[cind] = '$'
        else:
            incorrect_guesses.append(character)
            wrong += 1
        print ("Incorrect Guesses: "+" ".join(incorrect_guesses))
        print ((" ".join(board)))
        e = wrong + 1
        print ("\n".join(stages[0:e]))

        if "__" not in board:
            print ("You Win!")
            print (" ".join(board))
            win = True
            break
    if not win:
        print ("\n".join(stages[0:(wrong + 1)]))
        print ("You lose! It was {}.".format(word))

hangman(word)
