from chess_project.chess_piece import ChessPiece
from chess_project.white_pawn import WhitePawn
from chess_project.black_pawn import BlackPawn
from chess_project.rook import Rook
from chess_project.bishop import Bishop
from chess_project.board import c_board


class Game:

    def __init__(self):
        self.white_turn = True

    def take_move(self, start_position, end_position): #d2 d4
        start_row = ChessPiece.row_names[start_position[1]] #2 = 6
        start_col = ChessPiece.column_names[start_position[0]] #d = 3
        try:
            end_row = ChessPiece.row_names[end_position[1]] #4 = 4
            end_col = ChessPiece.column_names[end_position[0]] #d = 3
        except KeyError:
            return print("Invalid move")

        try:
            if self.white_turn and c_board.board[start_row][start_col].color == "white":
                c_board.board[start_row][start_col].move((end_row, end_col))
                self.white_turn = False
            elif not self.white_turn and c_board.board[start_row][start_col].color == "black":
                c_board.board[start_row][start_col].move((end_row, end_col))
                self.white_turn = True
            else:
                return print("Invalid move")
        except AttributeError:
            return print("Invalid move")


for row in range(8):
    for col in range(8):
        if c_board.board[row][col] == "p":
            c_board.board[row][col] = BlackPawn(row, col)
        elif c_board.board[row][col] == "P":
            c_board.board[row][col] = WhitePawn(row, col)
        elif c_board.board[row][col] == "r":
            c_board.board[row][col] = Rook(row, col, "black")
        elif c_board.board[row][col] == "R":
            c_board.board[row][col] = Rook(row, col, "white")
        elif c_board.board[row][col] == "b":
            c_board.board[row][col] = Bishop(row, col, "black")
        elif c_board.board[row][col] == "B":
            c_board.board[row][col] = Bishop(row, col, "white")


game1 = Game()

game1.take_move("d2", "d4")
c_board.print_board()

game1.take_move("c7", "c5")
c_board.print_board()

game1.take_move("d4", "c5")
c_board.print_board()

game1.take_move("a7", "a5")
c_board.print_board()

game1.take_move("a2", "a4")
c_board.print_board()

game1.take_move("a8", "a6")
c_board.print_board()

game1.take_move("a1", "a3")
c_board.print_board()

game1.take_move("a6", "b6")
c_board.print_board()

game1.take_move("a3", "b3")
c_board.print_board()

game1.take_move("b6", "b3")
c_board.print_board()

game1.take_move("c2", "b3")
c_board.print_board()

# game1.take_move("d7", "d6")
# c_board.print_board()
#
# game1.take_move("c1", "h6")
# c_board.print_board()
#
# game1.take_move("g7", "h6")
# c_board.print_board()
#
# game1.take_move("h2", "h3")
# c_board.print_board()
#
# game1.take_move("h2", "h3")
# c_board.print_board()
#
# game1.take_move("c8", "h3")
# c_board.print_board()

game1.take_move("c8", "d7")
c_board.print_board()