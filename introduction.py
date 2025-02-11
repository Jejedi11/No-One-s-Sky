import time
import sys
import click

def initialize():

    player_response = input("initialize? ")

    if player_response.lower() == "yes":
        print("Initializing...")
        time.sleep(5)
        print("Initialization complete.")

    elif player_response.lower() == "no":
        print("Initialization failed.")
        time.sleep(2)
        print("aborting...")
        time.sleep(1)
        sys.exit()

    else:
        print("Invalid response: Yes or No.")
        initialize()

def seek_shelter_ignore_warning():
    print("1. input coordinates")
    print("2. ignore warning")
    player_choice = input("What do you do? ")

    if player_choice.lower() == "1":
        click.clear()
        seek_shelter()

    elif player_choice.lower() == "2":
        click.clear()
        ignore_warning()

    else:
        print("Invalid response: 1 or 2")
        seek_shelter_ignore_warning()

# First branch of the storyline
def seek_shelter():
    print("Distance calculated: 6 km")
    input("Press enter to continue...")
    click.clear()
    print("I scan the nearby area for a path to the shelter.")

# Second branch of the storyline
def ignore_warning():
    print("I ignore the warning, I'll cut my own path.")
    input("Press enter to continue...")
    click.clear()
    print("I begin to walk in a random direction, I come across a gargantious animal.")
    input("Press enter to continue...")
    click.clear()
    print("The animal has tentacles that extrude from it's nose, the tentacles latch onto me.")
    input("Press enter to continue...")
    click.clear()
    creature_attack()
    
def creature_attack():
    print("1. Try to escape")
    print("2. Submit")
    print("3. Scream")
    player_response = input()

    if player_response == "1":
        print("I try to escape but the tentacles are too strong.")
        input("Press enter to continue...")
        click.clear()
        print("The animal drags me to it's nest, I am never seen again.")
        input("Press enter to continue...")
        click.clear()
        print("Game Over.")
        sys.exit()

    elif player_response == "2":
        print("I submit to the creature, it releases me.")
        input("Press enter to continue...")
        click.clear()
        print("The creature takes me to it's nest, I am never seen again.")
        input("Press enter to continue...")
        click.clear()
        print("Game Over.")
        sys.exit()

    elif player_response == "3":
        print("I scream for help, but no one is around to hear me.")
        input("Press enter to continue...")
        click.clear()
        print("The creature takes me to it's nest, I am never seen again.")
        input("Press enter to continue...")
        click.clear()
        print("Game Over.")
        sys.exit()

    else:
        print("Invalid response: 1, 2, or 3")
        creature_attack()

# Introduction storyline
click.clear()
print("hello world")
input("Press enter to continue...")
click.clear()
initialize()
input("Press enter to continue...")
click.clear()
player_name = input("Player not recognized. Please identify yourself: ")
print("Identification complete, welcome " + player_name + "!")
time.sleep(5)
click.clear()
print("I find myself on a strange planet, with no memory of how I got here (this is not insired by No Man's Sky).")
input("Press enter to continue...")
click.clear()
print("An electronic voice chimes from my spacesuit: Environmental dangers detected. Seeking shelter is advised")
input("Press enter to continue...")
click.clear()
print("A small screen on my suit's left arm flashes to life: Shelter detected.")
seek_shelter_ignore_warning()
