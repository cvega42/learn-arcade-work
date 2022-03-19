#Story texts to introduce gameplay----------------------------------

print("You are taking a tour of a house for rent.")
print("The rent is only $400 a month and you're a broke college student at Weber State")
print("The rent is too good to pass up, so you want to take a look around to see if it's too good to be true")
print("Type north, east, south, or west to navigate")

#Creating Room Classes-----------------------------------------------
class Room:
    description: ""
    north: "None"
    east: "None"
    south: "None"
    west: "None"

    def __init__(self, description, north=None, east=None, south=None, west=None):
        self.description = description
        self.north = north
        self.east = east
        self.west = west
        self.south = south

#Creating main functions for rooms------------------------------------
def main():
    room_list = []
    room = ["\nYou are in the south hallway. You can continue north to the north hallway or open the door to the east", 3, 1, None, None]
    room_list.append(room)
    room = ["\nYou have entered into the bathroom. Look at all the marble walls in the shower! From the bathroom, there are three doors.", 4, 2, None, 0]
    room_list.append(room)
    room = ["You are now in the dinning room! Plenty of room for a feast with family! You see two doors", 5, None, None, 1]
    room_list.append(room)
    room = ["You are now in the north hallway! There is a door to the east!", None, 4, 0, None]
    room_list.append(room)
    room = ["You are now in the master bedroom. There is a door to the north that leads to an amazing balcony!", 6, 5, 1, 3]
    room_list.append(room)
    room = ["You are now in the newly remodeled kitchen. There is a door to the west and south", None, None, 2, 4]
    room_list.append(room)
    room = ["Take that view in on this amazing balcony, you can see the Wasatch Mountains. Where to next?!", None, None, 4, None]
    room_list.append(room)

    current_room = 0

    done = False
    while not done:
        print(room_list[current_room][0])
        user_c = input("What direction do you want to go?")
        if user_c.lower() == "north" or user_c.lower() == "n":
            next_room = room_list[current_room][1]
            current_room = next_room
        elif user_c.lower() == "east" or user_c.lower() == "e":
            user_c = room_list[current_room][2]
            next_room = room_list[current_room][2]
            current_room = next_room
        elif user_c.lower() == "south" or user_c.lower() == "s":
            user_c = room_list[current_room][3]
            next_room = room_list[current_room][3]
            current_room = next_room
        elif user_c.lower() == "west" or user_c.lower() == "w":
            user_c = room_list[current_room][4]
            next_room = room_list[current_room][4]
            current_room = next_room
        elif user_c.lower() == "quit":
            print("Thanks for playing!")
            done = True
        else:
            print("I dont understand.")
        if user_c == None:
            print("You can't go that way.")

main()