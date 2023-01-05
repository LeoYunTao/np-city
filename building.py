class Building:  
    def __init__(self, location, buildingPoints = 0):
        self.location = location
        self.buildingPoints = buildingPoints
    
    def calculate_score(self):
        return 0

class Residential(Building):
    def __init__(self, location, buildingPoints=0):
        super().__init__(location, buildingPoints)

        self.name = "RES"

    def calculate_score(self, map):
        points = 0
        adjacent_buildings = map.get_adjacent_building(self.location)
        for adjacent_building in adjacent_buildings.values():
            if isinstance(adjacent_building, Residential) or isinstance(adjacent_building, Commercial):
                points += 1
            elif isinstance(adjacent_building, Park):
                points += 2
            elif isinstance(adjacent_building, Industry):
                points = 1
                break
            
        return points

class Industry(Building):
    def __init__(self, location, buildingPoints=0):
        super().__init__(location, buildingPoints)

        self.name = "IND"
        
    def calculate_score(self, map):
        points = 0
        points = map.count_building(self)
        return points
         
        
class Commercial(Building):
    def __init__(self, location, buildingPoints=0):
        super().__init__(location, buildingPoints)
        
        self.name = "COM"
        
    def calculate_score(self, map):
        return len([building for building in map.get_adjacent_building(self.location).values() \
            if building.name == self.name])

class Park(Building):
    def __init__(self, location, buildingPoints=0):
        super().__init__(location, buildingPoints)
        
        self.name = "PRK"
        
    def calculate_score(self, map):
        return len([building for building in map.get_adjacent_building(self.location).values() \
            if building.name == self.name])

class Road(Building):
    def __init__(self, location, buildingPoints=0):
        super().__init__(location, buildingPoints)
        
        self.name = "ROA"
        
    def calculate_score(self, map):
        count = 0
        
        searched = []
        stack = [map.get_building(self.location)]
        
        while len(stack) > 0:
            current_building = stack.pop()
            
            adjacent_buildings = map.get_adjacent_building(current_building.location).values()
            
            for adjacent_building in adjacent_buildings:
                if adjacent_building.location[1] != current_building.location[1]:
                    continue
                
                if adjacent_building.name != self.name:
                    continue
                
                if adjacent_building in searched:
                    continue
                
                stack.append(adjacent_building)
                count += 1
            
            searched.append(current_building)
            
        return count

class BuildingUtils:
    @staticmethod
    def choosePosition(map):

        buildErrorMsg = "Please type in a valid position map!"

        while True: # Check position
            pChoice = input("Select a position e.g A, 3: ").upper().split(",")

            pChoice = [i.strip() for i in pChoice] # remove trailing white spaces

            if len(pChoice) != 2:
                print(buildErrorMsg)
                continue

            if not pChoice[0].isalpha() or not pChoice[1].isdigit():
                print(buildErrorMsg)
                continue
            
            pChoice[1] = int(pChoice[1])
            pChoice = tuple(pChoice)
            
            if not map.is_location_empty(pChoice):
                print("Buildings already exists")
                continue
            
            if len(map.map) > 0 and not map.has_adjacent_building(pChoice):
                print("No Adjacent Building")
                continue

            return pChoice
                
    @staticmethod
    def buildBuilding(building, map):
        map.add_building(building)

    @staticmethod
    def selectBuilding(buildingDict, map):

        while True: # Check building type

            print("\n".join([f"({key}) {value.__name__}" for key, value in buildingDict.items()]))

            bChoice = input("\nYour choice: ").upper()

            if bChoice not in buildingDict:
                print("Please type in a valid building!")
                continue

            #map.draw_map()
            
            print("You have selected: " + buildingDict[bChoice].__name__)
            
            position = BuildingUtils.choosePosition(map)

            return buildingDict[bChoice](position)

