from libraries.Drivers.dc_driver.AMSpi import *
import RPi.GPIO as GPIO
import time

# ------ Tic-Tac-Toe ------ #

def constBoard(board):
    for i in range (0,9):
        if((i>0) and (i%3)==0):
            print("\n")
        if(board[i]==0):
            print("- ",end=" ")
        if (board[i]==1):
            print("O ",end=" ")
        if(board[i]==-1):    
            print("X ",end=" ")
    print("\n\n")

def user1Turn(board, amspi):
    pos=int(input("Enter X's position from [1...9]: "))
    if(board[pos-1]!=0):
        print("Space occupied, try again.")
        user1Turn(board, amspi)
    else:
        board[pos-1]=-1
        makeMove(pos, amspi)

def user2Turn(board, amspi):
    pos = int(input("Enter O's position from [1...9]: "))
    if(board[pos-1]!=0):
        print("Space occupied, try again.")
        user2Turn(board, amspi)
    else:
        board[pos-1]=1
        makeMove(pos, amspi)

def minimax(board,player):
    x=analyseBoard(board)
    if(x!=0):
        return (x*player)
    pos=-1
    value=-2
    for i in range(0,9):
        if(board[i]==0):
            board[i]=player
            score=-minimax(board,(player*-1))
            if(score>value):
                value=score
                pos=i
            board[i]=0
    if(pos==-1):
        return 0
    return value
    
    
def CompTurn(board, amspi):
    pos=-1
    value=-2
    for i in range(0,9):
        if(board[i]==0):
            board[i]=1
            score=-minimax(board, -1)
            board[i]=0
            if(score>value):
                value=score
                pos=i
    board[pos]=1
    makeMove(pos, amspi)


def analyseBoard(board):
    cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    for i in range(0,8):
        if(board[cb[i][0]] != 0 and
           board[cb[i][0]] == board[cb[i][1]] and
           board[cb[i][0]] == board[cb[i][2]]):
            return board[cb[i][2]]
    return 0

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
            if(analyseBoard(board)!=0):
                break
            if((i+player)%2==0):
                CompTurn(board, amspi)
            else:
                constBoard(board)
                user1Turn(board, amspi)
    else:
        for i in range (0,9):
            if(analyseBoard(board)!=0):
                break
            if((i)%2==0):
                constBoard(board)
                user1Turn(board, amspi)
            else:
                constBoard(board)
                user2Turn(board, amspi)
         
    x=analyseBoard(board)
    if(x==0):
        constBoard(board)
        print("Draw!")
    if(x==-1):
        constBoard(board)
        print("X Wins! O Lost!")
    if(x==1):
        constBoard(board)
        print("X Lost! O Wins!")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()