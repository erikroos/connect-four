class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.clear()

    def __repr__(self):
        """This method returns a string representation
           for an object of type Board.
        """
        s = ''
        for row in range(0, self.height):
            s += '|'
            for col in range(0, self.width):
                s += self.data[row][col] + '|'
            s += '\n'

        s += (2*self.width + 1) * '-'   # onderkant van het bord
        s += '\n '
        for col in range(0, self.width):
            s += str(col%10) + ' '

        return s
    
    def add_move(self, col, ox):
        for row in range(self.height-1, -1, -1):
            if self.data[row][col] == ' ':
                self.data[row][col] = ox
                return
            
    def add_move_while(self, col, ox):
        row = self.height - 1
        while row >= 0 and self.data[row][col] != ' ':
            row -= 1
        if self.data[row][col] == ' ': # strictly this check is not needed because it's guaranteed there's at least one free spot in this column
            self.data[row][col] = ox

    def clear(self):
        self.data = [[' '] * self.width for _ in range(self.height)]

    def set_board(self, move_string):
        """Accepts a string of columns and places
        alternating checkers in those columns,
        starting with 'X'.
        For example, call b.set_board('012345')
        to see 'X's and 'O's alternate on the
        bottom row, or b.set_board('000000') to
        see them alternate in the left column.
        move_string must be a string of one-digit integers.
        """
        next_checker = 'X'   # we starten door een 'X' te spelen
        for col_char in move_string:
            col = int(col_char)
            if 0 <= col <= self.width:
                self.add_move(col, next_checker)
            if next_checker == 'X':
                next_checker = 'O'
            else:
                next_checker = 'X'

    def allows_move(self, col):
        return self.data[0][col] == ' '

    def is_full(self):
        for col in range(self.width):
            if self.allows_move(col):
                return False
        return True
    
    def del_move(self, col):
        row = 0
        while self.data[row][col] == ' ' and row < self.height - 1:
            row += 1
        if row < self.height:
            self.data[row][col] = ' '
    

b = Board(2, 2)
print(b.is_full())
b.set_board('0011')
print(b)
print(b.is_full())
b.del_move(0)
b.del_move(0)
b.del_move(0)
print(b)