class Map:
    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column

        # map in format key: (x, y) value: building object
        self.map = {}
    
    def draw_map(self):
        for row in range(1, self.row):
            print("----" * self.row + "-")
            for column in [chr(i+65) for i in range(self.column)]:
                if column == 'A':
                    print("|", end="")
                    
                if self.is_location_empty((column, row)):
                    print("   ", end="|")
                else:
                    current_building = self.map[(column, row)]
                    print(current_building.name, end="|")

            print()
        print("----" * self.row + "-")
        
    # location in format (x, y)
    def is_location_empty(self, location):
        return location not in self.map
    
    def add_building(self, building):
        self.map[building.location] = building
    
    # check whether there is an adjecent building next to the location
    def has_adjecent_building(self, location):
        return (chr(ord(location[0]) - 1), location[1]) in self.map or \
                (location[0], location[1] - 1) in self.map or \
                (chr(ord(location[0]) + 1), location[1]) in self.map or \
                (location[0], location[1] + 1) in self.map
