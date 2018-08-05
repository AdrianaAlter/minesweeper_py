import tile

test_tile = tile.Tile()

def reset():
    test_tile.value = 0
    test_tile.bomb = False
    test_tile.flag = False
    test_tile.revealed = False

def test_tile_init():
    assert test_tile.value == 0
    assert test_tile.bomb == False
    assert test_tile.flag == False
    assert test_tile.revealed == False

def test_is_blank():
    assert test_tile.is_blank() == True
    test_tile.flag = True
    assert test_tile.is_blank() == False
    reset()

def test_is_flagged():
    assert test_tile.is_flagged() == False
    test_tile.flag = True
    assert test_tile.is_flagged() == True
    test_tile.revealed = True
    assert test_tile.is_flagged() == False
    reset()

def test_is_bombed():
    assert test_tile.is_bombed() == False
    test_tile.bomb = True
    assert test_tile.is_bombed() == False
    test_tile.revealed = True
    assert test_tile.is_bombed() == True
    reset()

def test_is_safely_flipped():
    assert test_tile.is_safely_flipped() == False
    test_tile.revealed = True
    assert test_tile.is_safely_flipped() == True
    test_tile.bomb = True
    assert test_tile.is_safely_flipped() == False
    reset()

def test_symbol():
    char = u"\u2B1B"
    assert test_tile.symbol(char) == char.encode('utf-8')

def test_inspect():
    assert test_tile.is_blank() == True
    assert test_tile.inspect() == test_tile.symbol(u"\u2B1B")
    test_tile.flag = True
    assert test_tile.inspect() == test_tile.symbol(u"\u2B50")
    reset()
    test_tile.revealed = True
    sym_string = u"\003" + str(test_tile.value)
    assert test_tile.inspect() == test_tile.symbol(sym_string) + " "
    test_tile.bomb = True
    assert test_tile.inspect() == test_tile.symbol(u"\u274C")
    reset()

def test_demarcate():
    line = test_tile.symbol(u"\u007C")
    char = (u"\u2B50")
    assert test_tile.demarcate(char) == line + test_tile.symbol(char) + line
