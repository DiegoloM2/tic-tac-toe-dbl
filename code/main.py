from sorting import Sorting
from TicTacToe.tic_tac_toe import *
from grid import *
from libraries.Drivers.dc_driver.AMSpi import *

GPIO.setwarnings(False)

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
            if gameChoice == 1:
                player = input("Enter to play 1(st) or 2(nd): ")
                player = int(player)

            gameTurn = 1



        if gameChoice == 1:

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
    time.sleep(0.3)

