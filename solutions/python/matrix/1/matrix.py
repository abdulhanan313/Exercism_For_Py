class Matrix:
    def __init__(self, matrix_string):
        self.rows = [
            [int(num) for num in row.split()]
            for row in matrix_string.split("\n")
        ]
        self.columns = [
            [row[i] for row in self.rows]
            for i in range(len(self.rows[0]))
        ]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]