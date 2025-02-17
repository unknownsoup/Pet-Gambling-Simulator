import random


class Pet:
    def __init__(self, balance, pet_type, pet_name, hunger, happiness, energy):
        self.balance = balance
        self.pet_type = pet_type
        self.pet_name = pet_name
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
        """
        Essentially, you make money through gambling, and you earn more money through taking care of your pet. 
        I want to add someway to spend your tokens 

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
        try:
            bet = int(input("Place bet: "))
            if bet <= 0:
                print("Invalid amount. Bet must be greater than 0.\n")
                return
        except ValueError:
            print("Invalid input. Please enter a valid number.\n")
            return
        try:
            option = int(input("What game do you want to play?\n"
                               "[1] Card Draw (1 in 4)\n"
                               "[2] Dice Game (1 in 6)\n"
                               "[3] Treasure Hunt (1 in 20)\n"
                               "You Choose: "))

            if option == 1:
                self.card_draw_game(bet)
            elif option == 2:
                self.dice_roll_game(bet)
            elif option == 3:
                self.treasure_chest_hunt_game(bet)
            else:
                print("Invalid option.\n")
        except ValueError:
            print("Invalid input. Not a valid number.\n")

