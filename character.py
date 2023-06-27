class Character:
    def __init__(self, name, description):
        """
        Initialize a Character object.

        Args:
            name (str): The name of the character.
            description (str): The description of the character.

        Attributes:
            name (str): The name of the character.
            description (str): The description of the character.
        """
        self.name = name
        self.description = description

    def talk(self):
        """
        Perform a talk action for the character.

        Behavior:
            - Prints the description of the character.
        """
        print(self.description)
