from tic_tac_toe import display_board, user1_turn
import pytest

def test_display_board():
    # Test case 1: Empty board
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    print("Test case 1:")
    disp = display_board(board)
    assert disp == """- - - \n- - - \n- - - \n\n"""

    # Expected output:
    # - - -
    # - - -
    # - - -

    # Test case 2: Board with 'O' and 'X' symbols
    board = [1, -1, 0, 0, 1, -1, 0, 0, 0]
    print("Test case 2:")
    disp = display_board(board)
    assert disp == """O X - \n- O X \n- - - \n\n"""

    # Expected output:
    # O X -
    # - O X
    # - - -

    # Test case 3: Board with all 'X' symbols
    board = [-1, -1, -1, -1, -1, -1, -1, -1, -1]
    print("Test case 3:")
    disp = display_board(board)
    assert disp == """X X X \nX X X \nX X X \n\n"""
    # Expected output:
    # X X X
    # X X X
    # X X X

def test_user1_turn(monkeypatch):
    """
    Test function for user1_turn().
    """
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Test case 1: Valid input
    monkeypatch.setattr('builtins.input', lambda _: '5') # simulates 'input' function
    assert user1_turn(board) == True
    assert board == [0, 0, 0, 0, -1, 0, 0, 0, 0]

    # Test case 2: Invalid input (occupied space)
    monkeypatch.setattr('builtins.input', lambda _: '5')
    assert user1_turn(board) == False
    assert board == [0, 0, 0, 0, -1, 0, 0, 0, 0]