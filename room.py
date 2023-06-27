class Room:
    def __init__(self, description, north, east, south, west):
        """
        Initialize a Room object.

        Args:
            description (str): The description of the room.
            north (Room): The room object to the north of the current room.
            east (Room): The room object to the east of the current room.
            south (Room): The room object to the south of the current room.
            west (Room): The room object to the west of the current room.

        Attributes:
            description (str): The description of the room.
            north (Room): The room object to the north of the current room.
            east (Room): The room object to the east of the current room.
            south (Room): The room object to the south of the current room.
            west (Room): The room object to the west of the current room.
            items (list): A list to store items present in the room.
            characters (list): A list to store characters present in the room.
        """
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
        self.items = []
        self.characters = []

    def __str__(self):
        """
        Return a string representation of the room.

        Returns:
            str: The description of the room, along with a list of items present (if any), and available paths.
        """
        paths = []
        if self.north:
            paths.append('north')
        if self.east:
            paths.append('east')
        if self.south:
            paths.append('south')
        if self.west:
            paths.append('west')
        
        paths_str = 'You can go: ' + ', '.join(paths) if paths else 'There are no paths.'

        return self.description + " " + ("Items here: " + ", ".join([item.name for item in self.items]) if self.items else "") + "\n" + paths_str
