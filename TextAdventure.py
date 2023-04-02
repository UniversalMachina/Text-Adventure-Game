def intro():
    print("Welcome to the Extended Text Adventure Game!")
    print("You find yourself in a dark room with two doors.")
    print("Do you want to go through door 1 or door 2?")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        room1()
    elif choice == "2":
        room2()
    else:
        print("Invalid choice. Please try again.")
        intro()

def room1():
    print("\nYou entered a room with a mysterious glowing orb.")
    print("Do you want to touch the orb (option 1) or leave the orb alone (option 2)?")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("\nThe orb teleported you to a room filled with gold coins.")
        print("Congratulations, you won!")
        play_again()
    elif choice == "2":
        print("\nYou left the orb alone and continued exploring.")
        room3()
    else:
        print("Invalid choice. Please try again.")
        room1()

def room2():
    print("\nYou entered a room with a sleeping dragon.")
    print("Do you want to sneak past the dragon (option 1) or fight the dragon (option 2)?")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        print("\nYou successfully sneaked past the dragon and found the hidden treasure!")
        print("Congratulations, you won!")
        play_again()
    elif choice == "2":
        print("\nYou fought the dragon and lost.")
        print("Game over!")
        play_again()
    else:
        print("Invalid choice. Please try again.")
        room2()

def room3():
    print("\nYou entered a room with three levers.")
    print("Which lever do you want to pull? (1, 2, or 3)")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        print("\nA hidden door opened, revealing a room full of treasure!")
        print("Congratulations, you won!")
        play_again()
    elif choice == "2":
        print("\nThe floor opened up beneath you, dropping you into a pit of spikes.")
        print("Game over!")
        play_again()
    elif choice == "3":
        print("\nThe room started to fill with water. You quickly ran back to the previous room.")
        intro()
    else:
        print("Invalid choice. Please try again.")
        room3()

def play_again():
    print("\nDo you want to play again? (yes or no)")

    choice = input("Enter yes or no: ")

    if choice.lower() == "yes":
        intro()
    elif choice.lower() == "no":
        print("Thanks for playing! Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        play_again()

intro()