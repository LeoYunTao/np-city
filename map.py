class Map:
    def __init__(self, row, column) -> None:
        self.row = row
        self.column = column

        # map in format key: (x, y) value: building object
        self.map = {}
    
    def draw_map(self):
        header_col = [chr(i+65) for i in range(self.column)]
        for y in header_col:
            print(" ", y, end=' ')
        print()
        for row in range(1, self.row+1):
            print("----" * self.row + "-")
            for column in [chr(i+65) for i in range(self.column)]:
                if column == 'A':
                    print("|", end="")

                if self.is_location_empty((column, row)):
                    print("   ", end="|")
                else:
                    current_building = self.map[(column, row)]
                    print(current_building.name, end="|")
            print("",  row)
        print("----" * self.row + "-")
    # location in format (x, y)
    def is_location_empty(self, location):
        return location not in self.map
    
    def add_building(self, building):
        self.map[building.location] = building
        
    def get_building(self, location):
        return self.map[location]
    
    # check whether there is an adjecent building next to the location
    def has_adjecent_building(self, location):
        return (chr(ord(location[0]) - 1), location[1]) in self.map or \
                (location[0], location[1] - 1) in self.map or \
                (chr(ord(location[0]) + 1), location[1]) in self.map or \
                (location[0], location[1] + 1) in self.map

    def get_adjecent_building(self, location):
        LEFT_LOCATION = (chr(ord(location[0]) - 1), location[1])
        RIGHT_LOCATION = (chr(ord(location[0]) + 1), location[1])
        TOP_LOCATION = (location[0], location[1] - 1)
        BOTTOM_LOCATION = (location[0], location[1] + 1)

        adjecent_buildings = {
            LEFT_LOCATION: self.map.get(LEFT_LOCATION, None),
            TOP_LOCATION: self.map.get(TOP_LOCATION, None),
            RIGHT_LOCATION: self.map.get(RIGHT_LOCATION, None),
            BOTTOM_LOCATION: self.map.get(BOTTOM_LOCATION, None)
        }

        #remove empty buildins
        return {key:val for key, val in adjecent_buildings.items() if val is not None}
