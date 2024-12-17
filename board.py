class Board:
    """A data type representing a Connect-4 board
       with an arbitrary number of rows and columns.
    """

    def __init__(self, width, height):
        """Construct objects of type Board, with the given width and height."""
        self.width = width
        self.height = height
        self.data = [[' ']*width for row in range(height)]

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


b = Board(7, 6)
b.add_move(0, 'X')
b.add_move(0, 'O')
b.add_move(0, 'X')
b.add_move(0, 'X')
b.add_move(3, 'O')
b.add_move(4, 'O')  # Valsspelen door O opnieuw te laten zetten!
b.add_move(5, 'O')
b.add_move(6, 'O')
print(b)