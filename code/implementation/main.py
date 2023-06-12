from sorting import Sorting
from TicTacToe.tic_tac_toe import *
from grid import *
from libraries.Drivers.dc_driver.AMSpi import *


amspi = AMSpi()
amspi.set_74HC595_pins(14, 15, 18)
amspi.set_L293D_pins(PWM0B=17, PWM0A=27, PWM2B=22)
sorter = Sorting()
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
gameChoice = -1
gameTurn = -1
player = -1

while True:
    # Determine whether it is time to sort
    if sorter.timeToSort():
        position = -1
        # If it is time to sort, sort the disk
        sorter.sort_disk()

        # Check if viewer has decided on how they want to play
        if gameChoice == -1:
            gameChoice = chooseGame()
            gameTurn = 1


        if gameChoice == 1:
            player = input("Enter to play 1(st) or 2(nd) :")
            player = int(player)

            if (gameChoice + player) % 2 == 1:
                board, position = CompTurn(board)
            else:
                display_board(board)
                board, position = player_turn(board, -1)  # Player 1's turn
            gameChoice += 1
        else:
            player = player * -1
            display_board(board)
            board, position = player_turn(player)

        makeMove(position, amspi)

        
        



    # Initialize the game board

    if choice == 1:
        print("Computer : O Vs. You : X")
        player = input("Enter to play 1(st) or 2(nd) :")
        player = int(player)

        for i in range(0, 9):
            if analyze_board(board) != 0:
                break

            if (i + player) % 2 == 0:
                CompTurn(board)

    else:
        for i in range(0, 9):
            if analyze_board(board) != 0:
                break
                
            if i % 2 == 0:
                display_board(board)
                player_turn(board, 1)  # Player 1's turn
            else:
                display_board(board)
                player_turn(board, -1)  # Player 2's turn

    x = analyze_board(board)
    if x == 0:
        display_board(board)
        print("Draw!!!")
    if x == -1:
        display_board(board)
        print("X Wins!!! Y Loose !!!")
    if x == 1:
        display_board(board)
        print("X Loose!!! O Wins !!!!")


