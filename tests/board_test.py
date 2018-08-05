import board
import random

test_board = board.Board()

def test_init():
    assert len(test_board.bomb_positions) == 0
    assert len(test_board.grid) == 9
    for row in test_board.grid:
        assert len(row) == 9

def test_place_bombs():
    assert len(test_board.bomb_positions) == 0
    test_board.place_bombs()
    assert len(test_board.bomb_positions) == 10
    assert uniq(test_board.bomb_positions) == True
    for set in test_board.bomb_positions:
        assert len(set) == 2
        assert set[0] < 10 and set[1] < 10
        assert test_board.grid[set[0]][set[1]].bomb == True

def uniq(arr):
    for checkIdx, checkEl in enumerate(arr):
        for i in range(checkIdx + 1, len(arr)):
            if checkEl[0] == arr[i][0] and checkEl[1] == arr[i][1]:
                return False
    return True

def test_get_neighbors():
    coords = [random.randint(3, 6), random.randint(3, 6)]
    assert len((test_board.get_neighbors(coords))) == 8

def test_get_valid_position():
    assert test_board.valid_position([0, 0]) == True
    assert test_board.valid_position([0, 8]) == True
    assert test_board.valid_position([8, 0]) == True
    assert test_board.valid_position([8, 8]) == True
    assert test_board.valid_position([0, 9]) == False
    assert test_board.valid_position([9, 0]) == False
    assert test_board.valid_position([9, 9]) == False
    assert test_board.valid_position([-1, 8]) == False
    assert test_board.valid_position([1, -8]) == False

def test_assign_values():
    test_board.place_bombs()
    test_board.assign_values()
    for set in test_board.bomb_positions:
        for neighbor in test_board.get_neighbors(set):
            assert test_board.grid[neighbor[0]][neighbor[1]].value > 0
