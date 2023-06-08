from libraries.Drivers.dc_driver.AMSpi import *
import RPi.GPIO as GPIO
import time
from TicTacToe.tic_tac_toe import *

# ------ Grid Control ------ #
    
def resetBoard(amspi):
    amspi.run_dc_motors([amspi.DC_Motor_3, amspi.DC_Motor_4])
    time.sleep(2.5)
    amspi.stop_dc_motors([amspi.DC_Motor_3, amspi.DC_Motor_4])

def positionTwo(amspi):
    amspi.run_dc_motors([amspi.DC_Motor_4], clockwise=False)
    time.sleep(0.8)
    amspi.stop_dc_motors([amspi.DC_Motor_4])

def positionThree(amspi):
    amspi.run_dc_motors([amspi.DC_Motor_4], clockwise=False)
    time.sleep(1.6)
    amspi.stop_dc_motors([amspi.DC_Motor_4])
    
def positionFour(amspi):
    amspi.run_dc_motors([amspi.DC_Motor_3], clockwise=False)
    time.sleep(0.65)
    amspi.stop_dc_motors([amspi.DC_Motor_3])
    
def positionFive(amspi):
    amspi.run_dc_motors([amspi.DC_Motor_3], clockwise=False)
    time.sleep(0.65)
    amspi.stop_dc_motors([amspi.DC_Motor_3])
    time.sleep(0.1)
    amspi.run_dc_motors([amspi.DC_Motor_4], clockwise=False)
    time.sleep(0.8)
    amspi.stop_dc_motors([amspi.DC_Motor_4])
    
def positionSix(amspi):
    amspi.run_dc_motors([amspi.DC_Motor_3], clockwise=False)
    time.sleep(0.65)
    amspi.stop_dc_motors([amspi.DC_Motor_3])
    time.sleep(0.1)
    amspi.run_dc_motors([amspi.DC_Motor_4], clockwise=False)
    time.sleep(1.6)
    amspi.stop_dc_motors([amspi.DC_Motor_4])

def positionSeven(amspi):
    amspi.run_dc_motors([amspi.DC_Motor_3], clockwise=False)
    time.sleep(1.3)
    amspi.stop_dc_motors([amspi.DC_Motor_3])
    
def positionEight(amspi):
    amspi.run_dc_motors([amspi.DC_Motor_3], clockwise=False)
    time.sleep(1.3)
    amspi.stop_dc_motors([amspi.DC_Motor_3])
    time.sleep(0.1)
    amspi.run_dc_motors([amspi.DC_Motor_4], clockwise=False)
    time.sleep(0.8)
    amspi.stop_dc_motors([amspi.DC_Motor_4])
    
def positionNine(amspi):
    amspi.run_dc_motors([amspi.DC_Motor_3], clockwise=False)
    time.sleep(1.3)
    amspi.stop_dc_motors([amspi.DC_Motor_3])
    time.sleep(0.1)
    amspi.run_dc_motors([amspi.DC_Motor_4], clockwise=False)
    time.sleep(1.6)
    amspi.stop_dc_motors([amspi.DC_Motor_4])
    
def runConveyor(amspi):
    amspi.run_dc_motors([amspi.DC_Motor_2], clockwise=False)
    time.sleep(3.5)
    amspi.stop_dc_motors([amspi.DC_Motor_2])

def makeMove(pos, amspi):
    if pos == 1:
        runConveyor(amspi)
    elif pos == 2:
        positionTwo(amspi)
        runConveyor(amspi)
        resetBoard(amspi)
    elif pos == 3:
        positionThree(amspi)
        runConveyor(amspi)
        resetBoard(amspi)
    elif pos == 4:
        positionFour(amspi)
        runConveyor(amspi)
        resetBoard(amspi)        
    elif pos == 5:        
        positionFive(amspi)
        runConveyor(amspi)
        resetBoard(amspi)
    elif pos == 6:
        positionSix(amspi)
        runConveyor(amspi)
        resetBoard(amspi)        
    elif pos == 7:
        positionSeven(amspi)
        runConveyor(amspi)
        resetBoard(amspi)        
    elif pos == 8:
        positionEight(amspi)
        runConveyor(amspi)
        resetBoard(amspi)        
    elif pos == 9:
        positionNine(amspi)
        runConveyor(amspi)
        resetBoard(amspi)        
        
def main():
    amspi = AMSpi()
    amspi.set_74HC595_pins(14, 15, 18)
    amspi.set_L293D_pins(PWM0B=17, PWM0A=27, PWM2B=22)
    
    resetBoard(amspi)
    
    choice= int(input("Enter 1 for single player, 2 for multiplayer: "))
    board=[0,0,0,0,0,0,0,0,0]
    
    if(choice==1):
        print("Computer : O Vs. You : X")
        player= int(input("Enter to play 1(st) or 2(nd) :"))
        for i in range (0,9):
            if(analyze_board(board)!=0):
                break
            if((i+player)%2==0):
                CompTurn(board)
            else:
                display_board(board)
                player_turn(board, -1)
    else:
        for i in range (0,9):
            if(analyze_board(board)!=0):
                break
            if((i)%2==0):
                display_board(board)
                player_turn(board, -1)
            else:
                display_board(board)
                player_turn(board, 1)
         
    x=analyze_board(board)
    if(x==0):
        display_board(board)
        print("Draw!")
    if(x==-1):
        display_board(board)
        print("X Wins! O Lost!")
    if(x==1):
        display_board(board)
        print("X Lost! O Wins!")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()