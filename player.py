import regex as re
import pandas as pd

def save_data(df, new_row):
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv('player_data.csv', index=False)


# creates new player by getting their name, password, pet, and pet name and saving it to database
def create_new_player(df):
    name_pattern = r"^[A-Za-z0-9]{3,15}$"
    ask1 = True
    while ask1:
        ask_name = input("Set Username: ")
        if re.match(name_pattern, ask_name):
            if df['Name'].isin([ask_name]).any():
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

    ask3 = True
    while ask3:
        print("What pet will you choose?!")
        for index, pet in enumerate(Player.pet_list):
            print(f"[{index + 1}] {pet}")

        try:
            pet_option = int(input("Your option: "))

            if 1 <= pet_option <= len(Player.pet_list):
                chosen_pet = Player.pet_list[pet_option - 1]
                print(f"You chose {chosen_pet}!")
                pet_name = input(f"What will your {chosen_pet}'s name be?\n"
                                 f"Keep in mind this will be their name FOREVER\n"
                                 f"and you cannot change this... EVER:")
                print(f"Welcome {ask_name}! and your {chosen_pet}, {pet_name}.\n")
                ask3 = False
            else:
                print("Invalid option. Please choose a valid number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


    # saving new player data to database
    new_row = pd.DataFrame(
        {'index': len(df), 'Name': [ask_name], 'Password': [ask_pass], 'Balance': 500, 'Pet': [chosen_pet], 'Pet_Name': [pet_name],
         'Hunger': 50, 'Happiness': 50, 'energy': 50})
    save_data(df, new_row)

    name_index = df[df['Name'] == ask_name].index[0]
    return name_index


# Gets existing user and verifies their password in the database
# Returns index of username
def grab_existing_player(df):
    # Name Verification
    while True:
        enter = input("Enter your username: ")
        if df['Name'].isin([enter]).any():
            print("Player Found.\n")
            name_index = df[df['Name'] == enter].index[0]
            break
        else:
            print("Player Not Found. Check casing\n")

    # Password Verification
    while True:
        pswrd = input("Enter your password: ")
        if df.iloc[name_index]['Password'] == pswrd:
            return name_index
        else:
            print("Password not correct.")


class Player:
    pet_list = ['Dog', 'Cat', 'Turtle', 'Chicken', 'Cow', 'Dragon']


    def __init__(self, name, password):
        self.name = name
        self.password = password


    def display_player_data(self):
        print(f"Name: {self.name}\n"
              f"Password: {self.password}")


    class Inventory:
        def __init__(self):
            self.items = []

        def add_item(self, item):
            self.items.append[item]
            print(f"Added {item} tp inventory.")


        def remove_item(self, item):
            if item in self.items:
                self.items.remove(item)
                print(f"Removed {item} from inventory.")
            else:
                print(f"{item} not found in inventory.")

