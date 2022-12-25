class Map:
    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column

        self.map = [[None] * column for _ in range(row)]
    
    def draw_map(self):
        for row in range(len(self.map)):
            print("----" * len(self.map) + "-")
            for column in range(len(self.map[0])):
                if column == 0:
                    print("|", end="")

                current_building = self.map[row][column]
                if current_building is None:
                    print("   ", end="|")
            print()
        print("----" * len(self.map) + "-")
