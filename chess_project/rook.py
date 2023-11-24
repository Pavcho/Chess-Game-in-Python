from chess_project.chess_piece import ChessPiece
from chess_project.board import c_board


class Rook(ChessPiece):
    moves_available = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
                       (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0),
                       (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
                       (0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7)]

    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color
        self.valid_moves = []

    def __str__(self):
        if self.color == "white":
            return "R"
        elif self.color == "black":
            return "r"

    def check_valid_moves(self):
        for r, c in Rook.moves_available[0:7]:
            if self.check_range(self.row + r, self.column + c):
                if c_board.board[self.row + r][self.column + c] == ".":
                    self.valid_moves.append((r, c))
                elif c_board.board[self.row + r][self.column + c].color != self.color:
                    self.valid_moves.append((r, c))
                    break
                elif c_board.board[self.row + r][self.column + c].color == self.color:
                    break
            else:
                break

        for r, c in Rook.moves_available[7:14]:
            if self.check_range(self.row + r, self.column + c):
                if c_board.board[self.row + r][self.column + c] == ".":
                    self.valid_moves.append((r, c))
                elif c_board.board[self.row + r][self.column + c].color != self.color:
                    self.valid_moves.append((r, c))
                    break
                elif c_board.board[self.row + r][self.column + c].color == self.color:
                    break
            else:
                break

        for r, c in Rook.moves_available[14:21]:
            if self.check_range(self.row + r, self.column + c):
                if c_board.board[self.row + r][self.column + c] == ".":
                    self.valid_moves.append((r, c))
                elif c_board.board[self.row + r][self.column + c].color != self.color:
                    self.valid_moves.append((r, c))
                    break
                elif c_board.board[self.row + r][self.column + c].color == self.color:
                    break
            else:
                break

        for r, c in Rook.moves_available[21:28]:
            if self.check_range(self.row + r, self.column + c):
                if c_board.board[self.row + r][self.column + c] == ".":
                    self.valid_moves.append((r, c))
                elif c_board.board[self.row + r][self.column + c].color != self.color:
                    self.valid_moves.append((r, c))
                    break
                elif c_board.board[self.row + r][self.column + c].color == self.color:
                    break
            else:
                break

    def move(self, new_position):
        self.check_valid_moves()

        if not self.valid_moves:
            return print("Invalid move!")

        new_row = new_position[0]
        new_col = new_position[1]

        diff = new_row - self.row
        diff2 = new_col - self.column

        for r, c in self.valid_moves:
            if r == diff and c == diff2:
                c_board.board[self.row][self.column] = "."
                self.row = new_row
                self.column = new_col
                c_board.board[self.row][self.column] = self
                break
        else:
            return print("Invalid move")
        self.valid_moves = []


