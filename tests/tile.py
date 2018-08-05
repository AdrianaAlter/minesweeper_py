class Tile(object):

    def __init__(self):
        self.bomb = False
        self.flag = False
        self.value = 0
        self.revealed = False

    def __repr__(self):
        return self.inspect()

    def inspect(self):
        if self.is_blank():
            return self.symbol(u"\u2B1B")
        elif self.is_safely_flipped():
            val = str(self.value)
            sym_string = u"\003" + val
            return self.symbol(sym_string) + " "
        elif self.is_flagged():
            return self.symbol(u"\u2B50")
        elif self.is_bombed():
            return self.symbol(u"\u274C")

    def symbol(self, char):
        return char.encode('utf-8')

    def demarcate(self, char):
        line = self.symbol(u"\u007C")
        return line + self.symbol(char) + line

    def is_blank(self):
        return not self.revealed and not self.flag

    def is_flagged(self):
        return self.flag and not self.is_safely_flipped()

    def is_bombed(self):
        return self.bomb and self.revealed

    def is_safely_flipped(self):
        return self.revealed and not self.is_bombed() and not self.bomb
