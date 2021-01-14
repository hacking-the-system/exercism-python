class Matrix:
    rows = []
    columns = []

    def __init__(self, matrix_string):
        self.rows = []
        self.columns = []
        for row in matrix_string.split("\n"):
            self.rows.append([int(val) for val in row.split(' ')])
        
        width = len(self.rows[0])
        height = len(self.rows)
        for x in range(width):
            matrix_col = []
            for y in range(height):
                matrix_col.append(self.rows[y][x])
            print(matrix_col)
            self.columns.append(matrix_col)                

    def row(self, index):
        return self.rows[index-1]

    def column(self, index):
        return self.columns[index-1]
