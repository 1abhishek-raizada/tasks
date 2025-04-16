
import tkinter as tk

class ChessGame:
    def __init__(self, root):
        self.root = root
        self.board = self.initialize_board()
        self.selected_piece = None
        
        self.create_chessboard()

    def initialize_board(self):
        # Empty 8x8 chess board
        board = [[' ' for _ in range(8)] for _ in range(8)]
        
        # Place the pieces on the board (using simplified single-letter notation)
        # Back rank (white)
        board[0] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        board[1] = ['P'] * 8
        # Empty squares
        board[2:6] = [[' ']*8 for _ in range(4)]
        # Back rank (black)
        board[6] = ['p'] * 8
        board[7] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        
        return board

    def create_chessboard(self):
        # Create a Tkinter grid of buttons to represent the chessboard
        self.buttons = {}
        for i in range(8):
            for j in range(8):
                square = tk.Button(self.root, width=8, height=4, command=lambda row=i, col=j: self.on_square_click(row, col))
                square.grid(row=i, column=j)
                # Alternate colors for the squares (light and dark)
                if (i + j) % 2 == 0:
                    square.config(bg="lightgray")
                else:
                    square.config(bg="darkgray")
                # Place the initial pieces on the board
                if self.board[i][j] != ' ':
                    square.config(text=self.board[i][j], font=("Arial", 24))
                self.buttons[(i, j)] = square

    def on_square_click(self, row, col):
        if self.selected_piece:
            self.move_piece(row, col)
        else:
            self.selected_piece = (row, col)
            self.highlight_square(row, col)

    def highlight_square(self, row, col):
        # Highlight the selected square
        self.buttons[(row, col)].config(bg="yellow")
    
    def move_piece(self, row, col):
        if self.board[row][col] == ' ':
            # Move the selected piece to the new position
            self.board[row][col] = self.board[self.selected_piece[0]][self.selected_piece[1]]
            self.board[self.selected_piece[0]][self.selected_piece[1]] = ' '
            # Update the button text and colors
            self.buttons[(self.selected_piece[0], self.selected_piece[1])].config(text=' ', bg="lightgray" if (self.selected_piece[0] + self.selected_piece[1]) % 2 == 0 else "darkgray")
            self.buttons[(row, col)].config(text=self.board[row][col], font=("Arial", 24))
            self.selected_piece = None
        else:
            # If the square is occupied, deselect the current piece
            self.selected_piece = None

def main():
    root = tk.Tk()
    root.title("Chess Game")
    game = ChessGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
