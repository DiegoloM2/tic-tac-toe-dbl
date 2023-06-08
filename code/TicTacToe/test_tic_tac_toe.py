from tic_tac_toe import display_board, player_turn, minimax, analyze_board
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

def test_player_turn(monkeypatch):
    """
    Test function for player_turn().
    """
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    # Test case 1: Input for first player "O"
    monkeypatch.setattr('builtins.input', lambda _: '5') # simulates 'input' function
    assert player_turn(board, 1) == True
    assert board == [0, 0, 0, 0, 1, 0, 0, 0, 0]

    # Test case 2: Input for second player (occupied space)
    monkeypatch.setattr('builtins.input', lambda _: '6')
    player_turn(board, -1)

    assert board == [0, 0, 0, 0, 1, -1, 0, 0, 0]



def test_minimax_for_draw():
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    player = 1
    assert minimax(board, player) == 0

def test_minimax_for_o_win():
    board = [1, 1, 0, -1, -1, 0, 0, 0, 0]
    player = 1
    assert minimax(board, player) == 1

def test_minimax_for_x_win():
    board = [1, -1, 1, 0, -1, 0, 0, 0, 0]
    player = -1
    assert minimax(board, player) == -1

def test_minimax_for_optimal_move():
    board = [1, -1, 0, 0, 0, 0, 0, 0, 0]
    player = 1
    assert minimax(board, player) == 1

def test_analyzeboard_for_no_win():
    board = [1, -1, 1, -1, 1, -1, -1, 1, -1]
    assert analyze_board(board) == 0

def test_analyzeboard_for_x_win():
    board = [-1, -1, -1, 0, 0, 0, 0, 0, 0]
    assert analyze_board(board) == -1

def test_analyzeboard_for_o_win():
    board = [1, 1, 1, 0, 0, 0, 0, 0, 0]
    assert analyze_board(board) == 1
