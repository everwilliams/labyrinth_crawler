# Ever Williams
# IT-140 Project Two
# Labyrinth Crawler - Text-Based Adventure Game

# ------------------------------
# ROOM MOVEMENT DATA
# ------------------------------
room_exits = {
    "Dusty Arrival Chamber": {
        "East": "Unkept Study",
        "South": "Witch's Kitchen"
    },
    "Unkept Study": {
        "West": "Dusty Arrival Chamber",
        "East": "Corridor to Nowhere",
        "South": "Hall of Toads"
    },
    "Corridor to Nowhere": {
        "West": "Unkept Study",
        "South": "Clock Room"
    },
    "Witch's Kitchen": {
        "North": "Dusty Arrival Chamber",
        "East": "Hall of Toads",
        "South": "Moss Garden"
    },
    "Hall of Toads": {
        "North": "Unkept Study",
        "West": "Witch's Kitchen",
        "East": "Clock Room",
        "South": "Mirror Ballroom"
    },
    "Moss Garden": {
        "North": "Witch's Kitchen",
        "East": "Mirror Ballroom"
    },
    "Mirror Ballroom": {
        "North": "Hall of Toads",
        "West": "Moss Garden",
        "East": "Goblin Throne Room"
    },
    "Clock Room": {
        "North": "Corridor to Nowhere",
        "West": "Hall of Toads",
        "South": "Goblin Throne Room"
    },
    "Goblin Throne Room": {
        "North": "Clock Room",
        "West": "Mirror Ballroom"
    }
}

# ------------------------------
# ROOM ITEM DATA (SEPARATED)
# ------------------------------
room_items = {
    "Unkept Study": "Spellbook",
    "Corridor to Nowhere": "Lost Sock",
    "Witch's Kitchen": "Rosemary Sprig",
    "Hall of Toads": "Goblin Charm",
    "Moss Garden": "Enchanted Soil",
    "Mirror Ballroom": "Mirror Ball",
    "Clock Room": "Gold Pendulum"
}

current_room = "Dusty Arrival Chamber"
inventory = []
required_items = 7

# ------------------------------
# FUNCTIONS
# ------------------------------

def intro_story():
    print("Welcome to Labyrinth Crawler!")
    print("----------------------------")
    print("You are whisked into a strange labyrinth ruled by the Goblin King.")
    input("Press Enter to begin your quest...\n")


def show_status():
    print("\n" + "-" * 40)
    print(f"You are in {current_room}")
    print(f"Inventory ({len(inventory)}/{required_items}): {inventory}")

    # Show exits
    exits = list(room_exits[current_room].keys())
    print("Available directions:", ", ".join(exits))

    # Show item if present
    if current_room in room_items:
        print(f"You see a {room_items[current_room]}")

    print("-" * 40)


def move_player(direction):
    direction = direction.title()

    if direction in room_exits[current_room]:
        return room_exits[current_room][direction]
    else:
        print("You cannot go that way!")
        return current_room


def get_item(command):
    global inventory

    parts = command.split(" ", 1)

    # Edge case: "get" with no item
    if len(parts) < 2 or not parts[1].strip():
        print("Specify an item to get.")
        return

    item_requested = parts[1].strip().lower()

    # Check if room has item
    if current_room not in room_items:
        print("There is no item in this room.")
        return

    actual_item = room_items[current_room]

    if item_requested == actual_item.lower():
        if actual_item in inventory:
            print("You already have that item.")
            return

        inventory.append(actual_item)
        del room_items[current_room]
        print(f"{actual_item} added to inventory.")
    else:
        print("That item is not in this room.")


def check_win_or_lose():
    if current_room == "Goblin Throne Room":
        if len(inventory) == required_items:
            print("Congratulations! You created the Goblinbane Potion!")
            print("The Goblin King is defeated! You win!")
        else:
            print("The Goblin King has charmed you!... GAME OVER!")
        print("Thanks for playing!")
        return True
    return False


def show_help():
    print("\nCommands:")
    print("  North, South, East, West")
    print("  Get <item name>")
    print("  Help\n")


# ------------------------------
# MAIN LOOP
# ------------------------------

def main():
    global current_room

    intro_story()

    while True:
        show_status()

        if check_win_or_lose():
            break

        command = input("Enter your action: ").strip()

        # Regression: blank input
        if not command:
            print("Please enter a command.")
            continue

        command_lower = command.lower()

        if command_lower == "help":
            show_help()

        elif command_lower.startswith("get"):
            get_item(command)

        elif command_lower in [d.lower() for d in room_exits[current_room]]:
            current_room = move_player(command)

        else:
            print("Invalid command. Type 'Help' for instructions.")


if __name__ == "__main__":
    main()