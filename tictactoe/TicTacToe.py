class TicTacToe:
    def __init__(self, size=3):
        self.turn = 0
        self.size = size
        self.signs = ["O", "X"]
        self.playground = [[None for r in range(self.size)] for c in range(self.size)]
    
    def __repr__(self):
        return "\n".join([str(x) for x in self.playground])
    
    def put(self, col, row, sign):
        assert row in range(self.size)
        assert col in range(self.size)
        assert self.playground[row][col] is None, "Field already taken"
        assert sign == self.signs[self.turn % len(self.signs)], "Not your turn"
        self.playground[row][col] = sign
        won = self._won()
        if won:
            print(f"🎉Congrats {won}, you won🎉")
        print(self)
        self.turn = self.turn + 1
    
    def _won(self):
        won = None
        for row in self.playground:
            won = row[0] if len(list(filter(lambda x: x == row[0], row))) == self.size else won
        
        rowsAsCols = [[self.playground[r][c] for r in range(self.size)] for c in range(self.size)]
        for row in rowsAsCols:
            won = row[0] if len(list(filter(lambda x: x == row[0], row))) == self.size else won
        
        diagAsCols = [[self.playground[r][r] for r in range(self.size)], [self.playground[r][(-1*r)-1] for r in range(self.size)]]
        for row in diagAsCols:
            won = row[0] if len(list(filter(lambda x: x == row[0], row))) == self.size else won
        return won


class Player:
    def __init__(self, ttt: TicTacToe, sign="X"):
        self.game = ttt
        self.sign = sign
        print("Lets play")
    def play(self):
        """
        Write a player strategy here
        In the end it should call 
        self.game.put(row, col, self.sign)
        """
        pass


class ArtificialPlayer(Player):
    def play(self):
        try:
            from random import randint
            row = randint(0, self.game.size - 1)
            col = randint(0, self.game.size - 1)
            self.game.put(row, col, self.sign)
        except AssertionError as e:
            if "Not your turn" not in str(e):
                self.play()
            else:
                print("Seems like its not my turn")


class LtrPlayer(Player):
    def play(self):
        for row_index in range(self.game.size):
            for col_index in range(self.game.size): 
                cell = self.game.playground[row_index][col_index]
                if cell is None:
                    self.game.put(col_index, row_index, self.sign)
                    return


class TtbPlayer(Player):
    def play(self):
        for col_index in range(self.game.size):
            for row_index in range(self.game.size):
                cell = self.game.playground[row_index][col_index]
                if cell is None:
                    self.game.put(col_index, row_index, self.sign)
                    return