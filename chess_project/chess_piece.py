from abc import ABC, abstractmethod

from chess_project.board import c_board


class ChessPiece(ABC):
    white_turn = True

    white_pieces = []
    black_pieces = []

    row_names = {'1': 7, '2': 6, '3': 5, '4': 4, '5': 3, '6': 2, '7': 1, '8': 0}
    column_names = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}

    possible_white_enpassant = ()
    possible_black_enpassant = ()

    def __init__(self, row, column, color):
        self.row = row
        self.column = column
        self.color = color
        self.valid_moves = []

    @staticmethod
    def check_range(r, c):
        if r > 7 or r < 0 or c > 7 or c < 0:
            return False
        else:
            return True

    def get_coordinates(self):
        return self.row, self.column

    def update_coordinates(self, updated_row, updated_column):
        c_board.board[self.row][self.column] = "."
        self.row = updated_row
        self.column = updated_column
        c_board.board[self.row][self.column] = self

    @staticmethod
    def check_if_white_in_check():
        attacked_squares = []
        king_row, king_col = None, None

        for piece in ChessPiece.black_pieces:
            cur_row, cur_col = piece.get_coordinates()
            if str(piece) == "p":
                attacked_squares.append((cur_row + 1, cur_col + 1))
                attacked_squares.append((cur_row + 1, cur_col - 1))
            else:
                valid_moves = piece.check_valid_moves()
                for move in valid_moves:
                    attacked_squares.append(move)

        for piece in ChessPiece.white_pieces:
            if str(piece) == "K":
                king_row, king_col = piece.get_coordinates()

        if (king_row, king_col) in attacked_squares:
            return True
        else:
            return False

    @staticmethod
    def check_if_black_in_check():
        attacked_squares = []
        king_row, king_col = None, None

        for piece in ChessPiece.white_pieces:
            cur_row, cur_col = piece.get_coordinates()
            if str(piece) == "P":
                attacked_squares.append((cur_row - 1, cur_col - 1))
                attacked_squares.append((cur_row - 1, cur_col + 1))
            else:
                valid_moves = piece.check_valid_moves()
                for move in valid_moves:
                    attacked_squares.append(move)

        for piece in ChessPiece.black_pieces:
            if str(piece) == "k":
                king_row, king_col = piece.get_coordinates()

        if (king_row, king_col) in attacked_squares:
            return True
        else:
            return False

    @staticmethod
    def updated_king_legal_moves(row, col, legal_moves):
        updated_valid_moves = []

        cur_row = row
        cur_col = col

        for move in legal_moves:
            new_row = move[0]
            new_col = move[1]
            c_board.board[cur_row][cur_col].move(new_row, new_col)

            if c_board.board[new_row][new_col].color == "white":
                if not ChessPiece.check_if_white_in_check():
                    updated_valid_moves.append(move)
                    c_board.board[new_row][new_col].move(cur_row, cur_col)

            elif c_board.board[new_row][new_col].color == "black":
                if not ChessPiece.check_if_black_in_check():
                    updated_valid_moves.append(move)
                    c_board.board[new_row][new_col].move(cur_row, cur_col)

        return updated_valid_moves

    @abstractmethod
    def check_valid_moves(self):
        pass

    def move(self, new_row, new_col):

        legal_moves = self.check_valid_moves()

        if not legal_moves:
            print("This piece has no legal moves!")
            return False

        if str(self) == "k" or str(self) == "K":
            legal_moves = ChessPiece.updated_king_legal_moves(self.row, self.column, legal_moves)
            if not legal_moves:
                print("This piece has no legal moves!")
                return False

        if (new_row, new_col) in legal_moves:

            if c_board.board[new_row][new_col] == ".":
                pass
            elif c_board.board[new_row][new_col] in ChessPiece.white_pieces:
                ChessPiece.white_pieces.remove(c_board.board[new_row][new_col])
            elif c_board.board[new_row][new_col] in ChessPiece.black_pieces:
                ChessPiece.black_pieces.remove(c_board.board[new_row][new_col])

            self.update_coordinates(new_row, new_col)

        else:
            print("This move is not legal!")
            return False

        return True



