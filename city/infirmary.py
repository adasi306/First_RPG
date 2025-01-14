from shelter import Shelter
import charakter_templates as ct
import json

try:
    with open("shelter_data.json", mode='r') as file:
        data = json.load(file)
except FileNotFoundError:
    with open("initial_shelter_settings.json", mode="r") as file1:
        data1 = json.load(file1)
    with open("shelter_data.json", mode="w") as file:
        json.dump(data1, file, indent=2)
finally:
    with open("shelter_data.json", mode='r') as file:
        data = json.load(file)

try:
    with open("player_inventory.json", mode='r') as file2:
        data_inventory = json.load(file2)
except FileNotFoundError:
    with open("player_inventory.json", mode="w") as file2:
        json.dump({"Money": 0}, file2, indent=2)
finally:
    with open("player_inventory.json", mode='r') as file2:
        data_inventory = json.load(file2)

try:
    with open("owned.json", mode='r') as file3:
        owned_heroes = json.load(file3)
except FileNotFoundError:
    with open("owned.json", mode="w") as file3:
        json.dump([], file3, indent=2)
finally:
    with open("owned.json", mode='r') as file3:
        owned_heroes = json.load(file3)

try:
    with open("trinkets.json", mode='r') as file3:
        owned_trinkets = json.load(file3)
except FileNotFoundError:
    with open("trinkets.json", mode="w") as file3:
        json.dump([], file3, indent=2)
finally:
    with open("trinkets.json", mode='r') as file3:
        owned_trinkets = json.load(file3)

try:
    with open("fallen_heroes.json", mode='r') as file3:
        fallen_heroes = json.load(file3)
except FileNotFoundError:
    with open("fallen_heroes.json", mode="w") as file3:
        json.dump([], file3, indent=2)
finally:
    with open("fallen_heroes.json", mode='r') as file3:
        fallen_heroes = json.load(file3)



class Infirmary(Shelter):
    def __init__(self):
        super().__init__()
        self.name = "Infirmary"
        self.enchant_path1_name = "Higher Standards"
        self.enchant_path2_name = "Lower Price"
        self.enchant_path1_req = ct.higher_standards_req
        self.enchant_path2_req = ct.lower_price_req
        self.enchant_path1_info = ct.higher_standards_info
        self.enchant_path2_info = ct.lower_price_info
        self.enchant_path1_level = data["Infirmary"]["path1"]["level"]
        self.enchant_path2_level = data["Infirmary"]["path2"]["level"]
        self.info = "Hi, let's try to fix your perks, we'll do our best. "

    def fixing_perk(self):
        loop = True
        while loop:
            self.clear_screen()
            for i, hero in enumerate(self.owned_heroes, start=1):
                if hero["positive perks"]:
                    print(f"{i}. {hero["name"]}, Class: {hero["class"]}, Level: {hero["level"]}")
                    print(f"Positive perks:\n{hero["positive perks"]}\n")
            print("Choose hero to fixing perk.")
            answer = input("[Q for Exit.]>>> ").lower()
            if answer == "q":
                break
            else:
                try:
                    self.clear_screen()
                    chosen_hero = self.owned_heroes[int(answer) - 1]
                    inner_loop = True
                    while inner_loop:
                        percentage = ct.lower_price[self.enchant_path2_level][1]
                        if self.percentage_random_chance(percentage):
                            print("winner!!!!!!!!!!!!!")
                            discount = ct.regular[0]
                        else:
                            discount = ct.lower_price[self.enchant_path2_level][0]
                        price = round(750 * discount)
                        print(f"{chosen_hero["name"]}, Class: {chosen_hero["class"]}, Level: {chosen_hero["level"]}")
                        perks = list(chosen_hero["positive perks"].items())
                        for i, (perk_name, perk_value) in enumerate(perks, start=1):
                            print(f"{i}. {perk_name}, Status: {perk_value}")
                            print(f"Effect:\n{ct.positive_perks_info[perk_name]}\n")
                        print()
                        print("Please choose perk to fix.")
                        ans = input("[Q for Exit.]>>> ").lower()
                        if ans == "q":
                            break
                        else:
                            try:
                                print(price)
                                perk_name_to_change = perks[int(ans) - 1][0]  # Get the key (perk name) by index
                                print(
                                    f"Selected perk: {perk_name_to_change} with status "
                                    f"{chosen_hero['positive perks'][perk_name_to_change]}")
                                new_value = None
                                if self.gold >= price:
                                    if chosen_hero["positive perks"][perk_name_to_change] == "unlocked":
                                        new_value = "locked"
                                    elif chosen_hero["positive perks"][perk_name_to_change] == "locked":
                                        new_value = "unlocked"
                                    chosen_hero["positive perks"][perk_name_to_change] = new_value
                                    print(f"{perk_name_to_change} Change status to: {new_value}")
                                    with open("owned.json", mode="w") as file3:
                                        json.dump(owned_heroes, file3, indent=2)
                                    self.gold -= price
                                    self.inventory["Money"] = self.gold
                                    data_inventory.update(self.inventory)
                                    with open("player_inventory.json", mode="w") as file2:
                                        json.dump(data_inventory, file2, indent=2)
                                else:
                                    self.clear_screen()
                                    print("You don't have enough ferrims.")
                                    self.press_any_key()
                            except IndexError:
                                self.clear_screen()
                                print("A perk with this number not exist.")
                                self.press_any_key()
                            except ValueError:
                                self.clear_screen()
                                print("Please provide some number instead of letters")
                                self.press_any_key()
                except IndexError:
                    self.clear_screen()
                    print("A hero with this number not exist.")
                    self.press_any_key()
                except ValueError:
                    self.clear_screen()
                    print("Please provide some number instead of letters")
                    self.press_any_key()

    def remove_negative_perk(self):
        loop = True
        while loop:
            self.clear_screen()
            for i, hero in enumerate(self.owned_heroes, start=1):
                print(f"{i}. {hero["name"]}, Class: {hero["class"]}, Level: {hero["level"]}")
                perks = list(hero["negative perks"].keys())
                print(f"Negative perks:{perks}\n")
            print("Choose hero to remove perk.")
            answer = input("[Q for Exit.]>>> ").lower()
            if answer == "q":
                break
            try:
                self.clear_screen()
                chosen_hero = self.owned_heroes[int(answer) - 1]
                inner_loop = True
                while inner_loop:
                    percentage = ct.lower_price[self.enchant_path2_level][1]
                    if self.percentage_random_chance(percentage):
                        print("winner!!!!!!!!!!!!!")
                        discount = ct.regular[0]
                    else:
                        discount = ct.lower_price[self.enchant_path2_level][0]
                    price = round(250 * discount)
                    print(f"{chosen_hero["name"]}, Class: {chosen_hero["class"]}, Level: {chosen_hero["level"]}")
                    perks = list(chosen_hero["negative perks"].keys())
                    for i, perk_name in enumerate(perks, start=1):
                        print(f"{i}. {perk_name}.")
                        print(f"Effect:\n{ct.negative_perks_info[perk_name]}\n")
                    print()
                    print(f"Cost: {price}. You have: {self.gold} Ferrims")
                    print("Please choose perk to remove.")
                    ans = input("[Q for Exit.]>>> ").lower()
                    if ans == "q":
                        break
                    else:
                        try:
                            print(price)
                            perk_name_to_change = perks[int(ans) - 1]
                            print(f"Selected perk: {perk_name_to_change} ")

                            if self.gold >= price:

                                self.remove_perk(chosen_hero, perk_name_to_change)

                                self.gold -= price
                                self.inventory["Money"] = self.gold
                                data_inventory.update(self.inventory)
                                with open("player_inventory.json", mode="w") as file2:
                                    json.dump(data_inventory, file2, indent=2)
                            else:
                                self.clear_screen()
                                print("You don't have enough ferrims.")
                                self.press_any_key()
                        except IndexError:
                            self.clear_screen()
                            print("A perk with this number not exist.")
                            self.press_any_key()
                        except ValueError:
                            self.clear_screen()
                            print("Please provide some number instead of letters")
                            self.press_any_key()
            except IndexError:
                self.clear_screen()
                print("A hero with this number not exist.")
                self.press_any_key()
            except ValueError:
                self.clear_screen()
                print("Please provide some number instead of letters")
                self.press_any_key()


    def healing_menu(self):
        loop = True
        while loop:
            self.clear_screen()
            print("1. Fixing positive perk.")
            print("2. Remove negative perk")
            print("Q. Exit.")
            answer = input(">>> ").lower()
            if answer == "q":
                break
            elif answer == "1":
                self.fixing_perk()
            elif answer == "2":
                self.remove_negative_perk()
            else:
                pass

    def menu(self):
        self.loop = True
        while self.loop:
            self.clear_screen()
            print(self.info)
            print("\n1. Healing.")
            print(f"2. {self.name} upgrade")
            print("Q. Exit")
            answer = input(">>> ").lower()
            if answer == "1":
                self.healing_menu()
            elif answer == "2":
                self.enchant_menu()
            elif answer == "q":
                self.loop = False
            else:
                pass
