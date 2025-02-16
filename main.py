"""
 --- Virtual Pet Simulator ---
Create a virtual pet that the player must take care of.
The pet has attributes like hunger, happiness, and energy,
which change over time or based on actions

1. Virtual Pet Simulator
Concept: Create a virtual pet that the player must take care of. The pet has attributes like hunger, happiness, and energy, which change over time or based on actions.

Classes: Pet, Food, Toys.

Features:
Save players with passwords
Feed your pet to reduce hunger.
Play with it to increase happiness.
Let it sleep to regain energy.
Add a lifecycle where the pet grows or can "die" if neglected.

Extra Fun: Make different pet types (dog, cat, dragon) with unique behaviors.

"""
import pygame as py
import pandas as pd
import regex as re
import time
import random
import math

data = pd.read_csv('player_data.csv')

def save_data(df, new_row):
    global data
    data = pd.concat([df, new_row], ignore_index=True)
    data.to_csv('player_data.csv', index=False)

# Create a new player option in main function
# Checks if name already exists then sets password
def create_new_player():
    name_pattern = r"^[A-Za-z0-9]{3,15}$"
    ask1 = True
    while ask1:
        ask_name = input("Set Username: ")
        if re.match(name_pattern, ask_name):
            if data['Name'].isin([ask_name]).any():
                print("Name already taken")
            else:
                ask1 = False
        else:
            print("Letters and numbers only. 3-15 character.\n")

    pass_pattern = r"^[A-Za-z0-9]{4,15}$"
    ask2 = True
    while ask2:
        ask_pass = input("Set Password: 4-15 Characters, A-Z, 0-9\nPassword: ")
        if re.match(pass_pattern, ask_pass):
            print("Password set successfully")
            ask2 = False
        else:
            print("Invalid Password. Directions ain't that hard bro\n")


    # saving new player data to database
    new_row = pd.DataFrame({'Name': [ask_name], 'Password': [ask_pass]})
    save_data(data, new_row)

    name_index = data[data['Name'] == ask_name].index[0]
    return name_index

# Gets existing user and verifies their password in the database
# Returns index of user name
def grab_existing_player():
    # Name Verification
    while True:
        enter = input("Enter your username: ")
        if data['Name'].isin([enter]).any():
            print("Player Found.\n")
            name_index = data[data['Name'] == enter].index[0]
            break
        else:
            print("Player Not Found. Check casing\n")

    # Password Verification
    while True:
        pswrd = input("Enter your password: ")
        if data.iloc[player_id]['Password'] == pswrd:
            return name_index
        else:
            print("Password not correct.")


class Player:
    def __init__(self, name, password):
        self.name = name
        self.password = password


class Pet:
    def __init__(self, balance, pet_type, hunger, happiness, energy):
        self.balance = balance
        self.pet_type = pet_type
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        """
        pets make money when they're happy
        pets dont make money when they're sad, unhappy, or tired
        
        """

    def lose_hunger(self, amount):
        self.hunger -= amount
        print(f"-{amount} food")

    def gain_hunger(self, amount):
        self.hunger += amount
        if amount > 1:
            print(f"+{amount} food")

    def lose_happy(self, amount):
        self.happiness -= amount
        print(f"-{amount} happiness")

    def gain_happy(self, amount):
        self.happiness += amount
        if amount > 1:
            print(f"+{amount} happiness")

    def lose_energy(self, amount):
        self.energy -= amount
        print(f"-{amount} energy")

    def gain_energy(self, amount):
        self.energy += amount
        if amount > 1:
            print(f"+{amount} energy")


    def add_money(self, amount):
        self.balance += amount
        print(f"+{amount}\n"
              f"Balance: {self.balance}")


    def subtract_money(self, amount):
        if (self.balance - amount) < 0:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"-{amount}\n"
                  f"Balance: {self.balance}")


    def play_with_pet(self):
        option = random.randint(1, 10)
        if option == (1 or 2 or 3):
            print(f"*Throws toy*\n"
                  f"...\n"
                  f"*{self.pet_type} doesn't seem very interested*\n")
            self.gain_happy(2)
            self.lose_energy(5)
            self.lose_hunger(5)

        elif option == 10:
            print(f"{self.pet_type} loves walks on the beach!\n")
            self.gain_happy(20)
            self.lose_energy(25)
            self.lose_hunger(10)

        else:
            print(f"You and your {self.pet_type} play tug-the-rope\n")
            self.gain_happy(5)
            self.lose_energy(15)
            self.lose_hunger(7)


    def feed_pet(self):
        option = random.randint(1, 10)
        if option == (1 or 2 or 3):
            print(f"... not a fan of carrots\n")
            self.gain_hunger(2)
            self.gain_energy(10)

        elif option == 10:
            print(f"Whats this quarter pounder with cheese\n"
                  f"doing in my pocket...\n")
            self.gain_hunger(20)
            self.gain_energy(15)

        else:
            print(f"Zaxbys 4 finger plate, no slaw, extra toast, extra sauce\n")
            self.gain_hunger(10)
            self.gain_energy(15)


    def dice_roll_game(self, bet):
        self.subtract_money(bet)
        print("Welcome to the Dice Roll Game!\n")
        player_guess = int(input("Guess the dice roll (1-6): "))
        roll_result = random.randint(1, 6)

        if player_guess < 1 or player_guess > 6:
            print("Invalid guess. Please choose a number between 1 and 6.")
            return

        print(f"The dice rolled: {roll_result}")
        if player_guess == roll_result:
            print("Spot on! You win!")
            self.add_money(bet * 3)
        else:
            print(f"Close! Try again next time.")


    def card_draw_game(self, bet):
        self.subtract_money(bet)
        print("Welcome to the Card Draw Game!")
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        player_guess = input("Guess the suit (Hearts, Diamonds, Clubs, Spades): ").strip().capitalize()

        if player_guess not in suits:
            print("Invalid guess. Please choose a valid suit.")
            return

        drawn_suit = random.choice(suits)
        print(f"The drawn card is from the suit: {drawn_suit}")
        if player_guess == drawn_suit:
            print("You're right! Lucky guess!")
            self.add_money(bet * 2)
        else:
            print("Not this time. Better luck next draw!")


    def treasure_chest_hunt_game(self, bet):
        self.subtract_money(bet)
        print("Welcome to the Treasure Chest Hunt!")
        print("There are 20 treasure chests. Choose one!")
        player_choice = int(input("Pick a chest (1-20): "))

        if player_choice < 1 or player_choice > 20:
            print("Invalid choice! Pick a chest between 1 and 20.")
            return

        print("Opening the chests...")
        treasure_chest = random.randint(1, 20)

        if player_choice == treasure_chest:
            print(f"Congratulations! You found the treasure in Chest #{treasure_chest}!")
            self.add_money(bet * 10)
        else:
            print(f"Sorry, the treasure was in Chest #{treasure_chest}. Better luck next time!")

    def play_game(self):
        bet = int(input("Place bet: "))
        if bet <= 0:
            print("Invalid amount\n")
            return
        elif ValueError:
            print("Invalid amount\n")

        option = random.randint(1, 3)
        if option == 1:
            self.dice_roll_game(bet)
        elif option == 2:
            self.card_draw_game(bet)
        elif option == 3:
            self.treasure_chest_hunt_game(bet)




def menu(id: int):
    running = True
    while running:
        print("Welcome to Virtual Pet Simulator!\n"
              "[0] New Player\n"
              "[1] Returning Player\n"
              "[2] Quit\n"
              "Enter your choice: ")

        choice = input()
        if choice == "0":
            player_id = create_new_player()
            return(player_id)
        elif choice == "1":
            player_id = grab_existing_player()
            return(player_id)
        elif choice == "2":
            running = False
        else:
            print("Invalid choice. Please try again.")


# Defining variables
MIN_STAT = 0
MAX_STAT = 100
player_id = 0
tick_interval = 10
last_tick = 0

# Starting menu - grabbing player ID
menu(player_id)
player_row = data.loc[data['index'] == player_id].iloc[0]
pet = Pet( # Creating pet & player instance
    player_row['Balance'],
    player_row['Pet'],
    player_row['Hunger'],
    player_row['Happiness'],
    player_row['energy']
)
player = Player(
    player_row['Name'],
    player_row['Password']
)

# Game loop
running = True
while running:

    choice = int(input(f"{player.name}'s {pet.pet_type} Stats:\n"
            f"Food: {pet.hunger}\n"
            f"Happiness: {pet.happiness}\n"
            f"Energy: {pet.energy}\n"
            f"\n"
            f"Balance: ${pet.balance}\n"
            f"\n"
            f"What would you like to do:\n"
            f"[1] Play with your pet\n"
            f"[2] Feed your Pet\n"
            f"[3] Play a game!\n"
            f"[4] Quit Game\n"))
    if choice == 1:
        pet.play_with_pet()
    elif choice == 2:
        pet.feed_pet()
    elif choice == 3:
        pet.play_game()
    elif choice == 4:
        data.loc[data['index'] == player_id, ['Name', 'Password', 'Balance', 'Pet', 'Hunger', 'Happiness', 'energy']] = \
            [player.name, player.password, pet.balance, pet.pet_type, pet.hunger, pet.happiness, pet.energy]
        data.to_csv('player_data.csv', index=False)
        running = False

    current_time = time.time()
    elapsed_time = current_time + tick_interval
    elap_sub_curr = elapsed_time - current_time
    decrease_amount = math.floor(elap_sub_curr / tick_interval)

    if current_time >= elapsed_time:
        # Perform "tick" updates... decrease stats
        print("--- "
              "While away:")
        pet.lose_happy(decrease_amount)
        pet.lose_hunger(decrease_amount)
        print("---")

