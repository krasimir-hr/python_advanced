class ConnectFour:
    def __init__(self):
        self.board = [[0 for x in range(7)] for _ in range(6)]
        self.current_player = 1

    def print_board(self):
        for row in self.board:
            print(row)

    def is_valid_move(self, column):
        return self.board[0][column] == 0

    def make_move(self, column):
        for row in range(5, -1, -1):
            if self.board[row][column] == 0:
                self.board[row][column] = self.current_player
                break

    def win_condition(self):
        # rows
        for row in range(6):
            for col in range(4):
                if self.board[row][col] == \
                        self.board[row][col + 1] == \
                        self.board[row][col + 2] == \
                        self.board[row][col + 3] != 0:
                    return self.board[row][col]

        # cols
        for row in range(3):
            for col in range(7):
                if self.board[row][col] == \
                        self.board[row + 1][col] == \
                        self.board[row + 2][col] == \
                        self.board[row + 3][col] != 0:
                    return self.board[row][col]

        #diags
        for row in range(3):
            for col in range(4):
                if self.board[row][col + 3] == \
                        self.board[row + 1][col + 2] == \
                        self.board[row + 2][col + 1] == \
                        self.board[row ][col + 3] != 0:
                    return self.board[row][col + 3]

        return None

    def play(self):
        while True:
            self.print_board()
            print(f"Player {self.current_player}, please choose a column")

            while True:
                column = int(input()) - 1
                if 0 <= column <= 6 and self.is_valid_move(column):
                    break
                print("Invalid move. Try again.")

            self.make_move(column)

            winner = self.win_condition()
            if winner:
                self.print_board()
                print(f"Player {winner} wins!")
                break

            if all(self.board[row][col] != 0 for row in range(6) for col in range(7)):
                self.print_board()
                print("It's a draw!")
                break

            self.current_player = 2 if self.current_player == 1 else 1


game = ConnectFour()
game.play()