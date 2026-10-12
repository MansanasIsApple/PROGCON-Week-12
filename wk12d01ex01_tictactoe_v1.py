# Name: Diesta, Macy T.
# Date: October 12, 2026
# Course: PROGCON IT261
# File: wk12d01ex01_tictactoe_v1.py
# Description: One-row Tic-Tac-Toe (3 boxes), user (O) vs computer (X).
#              Converted from my Flowgorithm file wk12d01ex01_tictactoe_v1.fprg.

import random


# Flowgorithm: Main
def main():
    # Flowgorithm: box1, box2, box3 start empty
    box1 = ""
    box2 = ""
    box3 = ""
    game_over = False       # Flowgorithm: gameOver = False
    move_count = 0          # Flowgorithm: moveCount = 0

    # Flowgorithm: randomNumber = Random(2) + 1 decides who starts
    random_number = random.randint(1, 2)
    if random_number == 1:
        current_player = "O"
        print("User (O) starts first")
    else:
        current_player = "X"
        print("Computer (X) starts first")

    # Flowgorithm: While gameOver = False
    while not game_over:
        if current_player == "O":
            # User turn: Output, Input chosenBox, then check each box
            print("User (O), choose a box (1-3): ")
            text = input()
            chosen_box = int(text) if text.strip().isdigit() else 0
        else:
            # Computer turn: chosenBox = Random(3) + 1
            chosen_box = random.randint(1, 3)

        # Flowgorithm: the chosen box must match the number and be empty
        placed = False
        if chosen_box == 1 and box1 == "":
            box1 = current_player
            placed = True
        elif chosen_box == 2 and box2 == "":
            box2 = current_player
            placed = True
        elif chosen_box == 3 and box3 == "":
            box3 = current_player
            placed = True

        if placed:
            move_count = move_count + 1
            if current_player == "X":
                print("Computer (X) chose box " + str(chosen_box))
            # Switch the turn only after a valid move
            if current_player == "O":
                current_player = "X"
            else:
                current_player = "O"
        elif current_player == "O":
            # Flowgorithm: invalid move, the user tries again
            print("Invalid move! Try again.")

        # Flowgorithm: show the board after each round
        print("[" + box1 + "] [" + box2 + "] [" + box3 + "]")

        # Flowgorithm: win check, all three boxes match and are not empty
        if box1 != "" and box1 == box2 and box2 == box3:
            print("Player " + box1 + " wins!")
            game_over = True
        # Flowgorithm: draw check, all 3 boxes are filled with no winner
        elif move_count == 3:
            print("It's a draw!")
            game_over = True

    print("Game over. Thanks for playing!")


if __name__ == "__main__":
    main()
