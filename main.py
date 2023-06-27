from room import Room
from item import Item
from character import Character
from player import Player
from backpack import BackPack  # Import the BackPack class


# Define rooms
swamp = Room("You're in a swamp. It's gross. There's a dangerous beast here.",
             None, None, None, None)
ruins = Room("You're in some old ruins.", None, None, swamp, None)
tree = Room("You're by a sacred tree.", None, swamp, None, None)
den = Room("You're in the python's den.", tree, None, None, ruins)

# Set exits for each room
swamp.north = ruins
swamp.west = tree
ruins.south = swamp
ruins.west = den
tree.east = swamp
tree.north = den
den.south = tree
den.east = ruins

# Add some items to the rooms
golden_egg = Item("Golden Python Egg", "An egg that shines brightly.")
den.items.append(golden_egg)
crystal_key = Item("Crystal Key", "A key made of sparkling crystal.")
ruins.items.append(crystal_key)

# Add some characters to the rooms
kaa = Character("Kaa", "I am Kaa, the Python Spirit.")
den.characters.append(kaa)
tribe_leader = Character(
    "Tribe Leader", "I am the leader of the Ancient Tribe.")
tree.characters.append(tribe_leader)

# Game instructions
print("---------------------------------------------------------------------------------------------------------")
print("Welcome to the Jungle Adventure Game!")
print("You must navigate through the jungle, picking up items along the way.")
print("The commands you can use are: 'go [direction]', 'take [item]'")
print("Your goal is to find the Golden Python Egg and the Crystal Key, then present them to the Tribe Leader at the Sacred Tree.")
print("But beware! There are dangers in the jungle that could lead to your downfall...\n")
print("---------------------------------------------------------------------------------------------------------")

# Start game
player = Player(den, swamp)

while True:
    print(player.location)  # Print the whole Room object



    command = input("> ").split()

    action = command[0].lower()

    if action == "go":
        player.move(command[1].lower())
    elif action == "take":
        player.take_item(" ".join(command[1:]))
    elif action == "talk":
        player.talk_to(" ".join(command[1:]))

    # Check win condition
    if player.location == tree and player.has_item("Golden Python Egg") and player.has_item("Crystal Key"):
        print("You presented the items to the tribe leader and won the game!")
        break
