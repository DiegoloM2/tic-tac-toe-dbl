"""This is a file that tests the 'main' program by executing without the use of hardware"""

from sorting import Sorting
from libraries.TicTacToe.tic_tac_toe import *
from libraries.Grid.grid import *
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
    won = analyze_board(board) in [1, -1]
    if gameTurn > 9 or won:
        board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        gameChoice = -1
        gameTurn = -1
        player = -1
        print("--------\nTHIS GAME HAS FINISHED, PLEASE TAKE THE DISKS OF THE GRID AND TYPE any key once your finished so we can continue")
        input()


    position = -1
    # If it is time to sort, sort the disk
    # sorter.sort_disk()

    # Check if viewer has decided on how they want to play
    if gameChoice == -1:
        gameChoice = chooseGame()
        if gameChoice == 1:
            player = input("Enter to play 1(st) or 2(nd): ")
            player = int(player)
        gameTurn = 1



    if gameChoice == 1:

        if (gameTurn + player) % 2 == 1:
            print("\n--- COMPUTER'S MOVE ---\n")
            board, position = CompTurn(board)
            
            # Add index for makeMove function since it uses one index and minmax uses zero-index.
            position += 1
        else:
            
            print("--- PLAYER'S MOVE ---")
            board, position = player_turn(board, -1)  # Player 1's turn
    else:
        print(f"--- PLAYER {player}'S MOVE ---")

        player = player * -1
        board, position = player_turn(board, player)

    # makeMove(position, amspi)
    print("--- FINISHED EXECUTING MOVE ---\n")
    print("\nCURRENT STATE OF BOARD")
    display_board(board)
    print("\n---- CHECKING FOR THE NEXT DISK ----\n\n")
    gameTurn += 1



    time.sleep(0.3)



