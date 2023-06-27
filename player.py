from backpack import BackPack


class Player:
    def __init__(self, start_location, swamp):
        """
        Initialize a Player object.

        Args:
            start_location (Room): The starting location of the player.
            swamp (Room): The swamp room object.

        Attributes:
            inventory (BackPack): A backpack to store the items collected by the player.
            location (Room): The current location of the player.
            swamp (Room): The swamp room object.
        """
        self.inventory = BackPack()
        self.location = start_location
        self.swamp = swamp

    def move(self, direction):
        """
        Move the player in the specified direction.

        Args:
            direction (str): The direction in which the player wants to move.

        Behavior:
            - If the player tries to move east from the swamp without the "Golden Python Egg" item,
              the game is lost.
            - Otherwise, the player's location is updated based on the specified direction.
        """
        if direction == 'east' and self.location == self.swamp and not self.has_item("Golden Python Egg"):
            print("The beast attacked you! You lost the game.")
            exit()
        self.location = getattr(self.location, direction)

    def take_item(self, item_name):
        """
        Take an item from the current location.

        Args:
            item_name (str): The name of the item to take.

        Behavior:
            - If the item exists at the current location:
                - If the item is the "Golden Python Egg" and the player does not have the "Crystal Key",
                  a message is printed indicating the egg is too hot to touch.
                - Otherwise, the item is added to the player's inventory and removed from the location.
                  A message is printed to confirm the item has been taken.
            - If the item does not exist at the current location, a message is printed indicating it's not there.
        """
        item = next((item for item in self.location.items if item.name.lower(
        ) == item_name.lower()), None)

        if item:
            if item.name == "Golden Python Egg" and not self.has_item("Crystal Key"):
                print(
                    "The egg is too hot to touch! Maybe there's something that can help you pick it up.")
            else:
                self.inventory.add(item)
                self.location.items.remove(item)
                print(f"You have taken the {item_name}.")
        else:
            print("That item is not here.")

    def has_item(self, item_name):
        """
        Check if the player has a specific item in their inventory.

        Args:
            item_name (str): The name of the item to check.

        Returns:
            bool: True if the player has the item, False otherwise.
        """
        return self.inventory.in_backpack(item_name)

    def talk_to(self, character_name):
        """
        Talk to a character at the current location.

        Args:
            character_name (str): The name of the character to talk to.

        Behavior:
            - If the character exists at the current location, their talk method is called.
            - If the character does not exist at the current location, a message is printed indicating they're not there.
        """
        character = next((character for character in self.location.characters if character.name.lower(
        ) == character_name.lower()), None)

        if character:
            character.talk()
        else:
            print("That character is not here.")
