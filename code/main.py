from libraries.Sorting.sorting import Sorting
from libraries.TicTacToe.tic_tac_toe import *
from libraries.Grid.grid import *
from libraries.Drivers.dc_driver.AMSpi import *

# Disable GPIO warnings
GPIO.setwarnings(False)

# Initialize AMSpi instance
amspi = AMSpi()

# Set the pins for 74HC595 shift register
amspi.set_74HC595_pins(21, 20, 16)

# Set the pins for L293D motor driver
amspi.set_L293D_pins(PWM0B=5, PWM0A=13, PWM2B=19)

# Create Sorting instance for disk sorting
sorter = Sorting()

# Create an empty Tic Tac Toe board
board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# Initialize game variables
gameChoice = -1
gameTurn = -1
player = -1

# Reset the game board to start playing
reset_board(amspi)
    
def reset_game():
    """
    Resets the game state by resetting the board and game variables.
    """
    global board, gameChoice, gameTurn, player
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    gameChoice = -1
    gameTurn = -1
    player = -1
    
    
def game_finished(board, gameTurn):
    """
    Checks if the game has finished.
    """
    won = analyze_board(board) in [1, -1]
    if gameTurn > 9 or won: return True
    return False


def play_game():
    """
    Starts and manages the main loop.
    """
    global board, gameChoice, gameTurn, player

    while True:
        if game_finished(board, gameTurn):
            reset_game()
            print("--------\nTHIS GAME HAS FINISHED, PLEASE TAKE THE DISKS OFF THE GRID AND TYPE any key once you're finished so we can continue")
            input()
        
        if sorter.timeToSort():
            position = -1
            
            # If it's time to sort, sort the disk
            sorter.sort_disk()
            
            # Check if player has chosen the game mode
            if gameChoice == -1:
                gameChoice = chooseGame()
                if gameChoice == 1:
                    player = input("Enter 1 to play first or 2 to play second: ")
                    player = int(player)
                gameTurn = 1
    
            if gameChoice == 1:
                if (gameTurn + player) % 2 == 1:
                    print("\n--- COMPUTER'S MOVE ---\n")
                    board, position = CompTurn(board)
                    
                    # Adjust the position to use one-index for makeMove function
                    position += 1
                else:
                    print("--- PLAYER'S MOVE ---")
                    board, position = player_turn(board, -1)  # Player 1's turn
            else:
                print(f"--- PLAYER {player}'S MOVE ---")
                player = player * -1
                board, position = player_turn(board, player)
    
            makeMove(position, amspi)
            print("--- FINISHED EXECUTING MOVE ---\n")
            print("\nCURRENT STATE OF BOARD")
            display_board(board)
            print("\n---- CHECKING FOR THE NEXT DISK ----\n\n")
            gameTurn += 1
    
        time.sleep(0.3)	

play_game()




