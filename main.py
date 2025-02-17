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

from pet import Pet
from player import Player
from player import create_new_player, grab_existing_player

import pandas as pd
import regex as re
import time
import random
import math

data = pd.read_csv('player_data.csv')

def menu():
    global switch
    running = True
    while running:
        print("Welcome to Virtual Pet Simulator!\n"
              "[0] New Player\n"
              "[1] Returning Player\n"
              "[2] Quit\n"
              "Enter your choice: ")

        choice = input()
        if choice == "0":
            player_id = create_new_player(data)
            return(player_id)
        elif choice == "1":
            player_id = grab_existing_player(data)
            return(player_id)
        elif choice == "2":
            switch = True
            running = False
        else:
            print("Invalid choice. Please try again.")

def game_loop(player_id):
    # Defining variables
    MIN_STAT = 0
    MAX_STAT = 100
    tick_interval = 10
    last_tick = 0

    # Starting menu - grabbing player ID
    player_id = menu()
    player_row = data.loc[data['index'] == player_id].iloc[0]
    pet = Pet( # Creating pet & player instance
        player_row['Balance'],
        player_row['Pet'],
        player_row['Pet_Name'],
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
            data.loc[data['index'] == player_id, ['Name', 'Password', 'Balance', 'Pet', 'Pet_Name', 'Hunger', 'Happiness', 'energy']] = \
                [player.name, player.password, pet.balance, pet.pet_type, pet.pet_name, pet.hunger, pet.happiness, pet.energy]
            data.to_csv('player_data.csv', index=False)
            running = False

        """
        
        I cant get this tick system to work so I'm leaving 
        it here for if I write this using pygame
        
        current_time = time.time()
        elapsed_time = current_time - last_tick

        if elapsed_time >= tick_interval:
            decrease_amount = math.floor(elapsed_time / tick_interval)
            print("--- While Away ---")
            pet.lose_hunger(decrease_amount)
            pet.lose_happy(decrease_amount)
            pet.lose_energy(decrease_amount)
            last_tick = current_time
            print("------------------")
            
        """

def main():
    while True:
        player_id = menu()
        if player_id is None:
            print("Thanks for playing, Goodbye!")
            break
        game_loop(player_id)

if __name__ == "__main__":
    main()

print("Program Closed Successfully")
