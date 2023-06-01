from math import ceil


class TicTacToe:
    def __init__(self):
        self.board = [[" " for x in range(3)] for _ in range(3)]
        self.player_one_name = input("Player one name: ")
        self.player_two_name = input("Player two name: ")
        self.player_one_sign = input(f"{self.player_one_name}, would you like to play with 'X' or 'O'? ")
        while self.player_one_sign != "X" and self.player_one_sign != "O":
            self.player_one_sign = input(f"{self.player_one_name}, please choose either 'X' or 'O'.")
        self.player_two_sign = "X" if self.player_one_sign == "O" else "O"
        self.player_one = [self.player_one_name, self.player_one_sign]
        self.player_two = [self.player_two_name, self.player_two_sign]
        self.score = {self.player_one[0]: 0, self.player_two[0]: 0, "Draws": 0}
        self.current = self.player_one
        self.current_starter = self.current

    def print_board(self):
        for row in self.board:
            print("|  ", end="")
            print("  |  ".join([str(x) for x in row]), end="")
            print("  |")

    def print_score(self):
        for player, score in self.score.items():
            print(f"{player}: {score}")

    def check_if_won(self):
        # rows
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == self.current[1]:
                return True

        # cols
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == self.current[1]:
                return True

        # diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current[1]:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current[1]:
            return True

        return False

    def play(self):
        self.current = self.current_starter
        print("This is the numeration of the board:")
        print("|  1  |  2  |  3  |")
        print("|  4  |  5  |  6  |")
        print("|  7  |  8  |  9  |")
        print(f"{self.current[0]} starts first!")
        while True:
            try:
                choice = int(input(f"{self.current[0]} choose a free position [1-9]: "))
            except ValueError:
                print("Please choose a number from 1 to 9")
                continue

            if choice < 1 or choice > 9:
                print("Please choose a number from 1 to 9.")
                continue

            row = ceil(choice / 3) - 1
            col = choice % 3 - 1
            if self.board[row][col] != " ":
                print("Invalid move. Try again.")
                continue

            self.board[row][col] = self.current[1]
            self.print_board()

            if self.check_if_won():
                print(f"{self.current[0]} won!")
                self.score[self.current[0]] += 1
                self.print_score()
                self.restart_game()
                break

            if all(self.board[i][j] != " " for i in range(3) for j in range(3)):
                print("It's a tie!")
                self.score["Draws"] += 1
                self.print_score()
                self.restart_game()
                break

            self.current = self.player_two if self.current == self.player_one else self.player_one

    def restart_game(self):
        choice = input("Do you want to play again? (yes/no): ")
        if choice.lower() == "yes":
            self.board = [[" " for x in range(3)] for _ in range(3)]
            self.current_starter = self.player_two if self.current_starter == self.player_one else self.player_one
            self.play()
        else:
            print("Thank you for playing!")


game = TicTacToe()
game.play()
