from shelter import Shelter
import charakter_templates as ct
import trinkets as tr
import json, random

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


class FortuneTellingChamber(Shelter):
    def __init__(self):
        super().__init__()
        self.name = "Fortune Telling Chamber"
        self.enchant_path1_name = "Better Shine"
        self.enchant_path2_name = "More Flash"
        self.enchant_path1_req = ct.better_shine_req
        self.enchant_path2_req = ct.more_flash_req
        self.enchant_path1_info = ct.better_shine_info
        self.enchant_path2_info = ct.more_flash_info
        self.enchant_path1_level = data["Fortune Telling Chamber"]["path1"]["level"]
        self.enchant_path2_level = data["Fortune Telling Chamber"]["path2"]["level"]
        self.info = "Welcome great warrior. hm... Do you want to buy something?"
        self.offered_trinkets = None
    def show_offered_trinkets(self):
        for number in range(len(self.offered_trinkets)):
            nr = number + 1
            trinket = self.offered_trinkets[number]
            cost = round(tr.trinkets_stats[trinket]["cost"] * ct.better_shine[self.enchant_path1_level][4])
            rarity = tr.trinkets_stats[trinket]["rarity"]
            print(f"{nr} . {trinket}, Rarity: {rarity}, Cost: {cost} Ferrims")
            print(f"Effect: {tr.trinkets_info[trinket]["effect"]}")

    def buying_trinkets(self):
        self.loop = True
        while self.loop:
            self.clear_screen()
            self.show_offered_trinkets()
            if len(self.offered_trinkets) > 0:
                print(f"\nYou have {self.gold} Ferrims.")
                print(f"Which trinket do you wish to buy ?")
                quest = input("Q for exit. >>> ")
                if quest == "q":
                    break
                elif len(self.offered_trinkets) > 0:
                    try:
                        number = int(quest) - 1
                        trinket = self.offered_trinkets[number]
                        price = tr.trinkets_stats[trinket]["cost"]
                        cost = round(price * ct.better_shine[self.enchant_path1_level][4])
                        if self.gold >= cost:
                            datas = trinket
                            owned_trinkets.append(datas)
                            with open("trinkets.json", mode="w") as file:
                                json.dump(owned_trinkets, file, indent=2)
                            self.offered_trinkets.pop(number)
                            self.gold -= cost
                            self.inventory["Money"] = self.gold
                            data_inventory.update(self.inventory)
                            with open("player_inventory.json", mode="w") as file2:
                                json.dump(data_inventory, file2, indent=2)
                        else:
                            self.clear_screen()
                            print("You don't have enough money")
                            self.press_any_key()
                    except ValueError:
                        self.clear_screen()
                        print("Please provide some number instead of letters")
                        self.press_any_key()
                    except IndexError:
                        self.clear_screen()
                        print("There is no item under this number.")
                        self.press_any_key()
                else:
                    pass
            else:

                print("\nYou already bought everything...")
                self.press_any_key()
                break

    def trinket_shop(self):
        self.reload_inventory()
        if self.inventory["Glittering Coin"] > 0:
            self.nr_offered_trinkets = ct.more_flash[self.enchant_path2_level]
            self.offered_trinkets = []
            for number in range(self.nr_offered_trinkets):
                a = ct.better_shine[self.enchant_path1_level][0]
                b = ct.better_shine[self.enchant_path1_level][1]
                c = ct.better_shine[self.enchant_path1_level][2]
                d = ct.better_shine[self.enchant_path1_level][3]
                self.probability(a, b, c, d)
                trinket = random.choice(tr.trinkets[self.probability_winner])
                self.offered_trinkets.append(trinket)
            self.inventory["Glittering Coin"] = 0
            datas = {"Glittering Coin": 0}
            data_inventory.update(datas)
            with open("player_inventory.json", mode="w") as file2:
                json.dump(data_inventory, file2, indent=2)
            self.buying_trinkets()

        else:
            self.buying_trinkets()

    def display_trinkets(self, rarity):
        trink_storage = []
        trink_in_use = []
        trink_storage_counted = []
        counter = {}
        for trinket in owned_trinkets:
            if tr.trinkets_stats[trinket]["rarity"] == rarity:
                trink_storage.append(trinket)
        for element in trink_storage:
            counter[element] = trink_storage.count(element)
        for key, value in counter.items():
            trink_storage_counted.append({"name": key, "details": {"worn": None, "amount": value}})
        for hero in self.owned_heroes:
            for trinket in hero["trinkets"]:
                if tr.trinkets_stats[trinket]["rarity"] == rarity:
                    trink_in_use.append({"name": trinket, "details": {"worn": hero["name"], "amount": None}})
        trinkets_to_display = trink_in_use + trink_storage_counted
        self.clear_screen()
        for i, trinket in enumerate(trinkets_to_display, start=1):
            if i % 5 != 0:
                if trinket["details"]["worn"] is not None:
                    print(f"{i}. {trinket["name"]}, Worn by: {trinket["details"]["worn"]}")
                    print(f"Effect: {tr.trinkets_info[trinket["name"]]["effect"]}")
                    print(f"Disassembly: {tr.trinkets_info[trinket["name"]]["disassembly"]}")
                    print()
                if trinket["details"]["amount"] is not None:
                    print(f"{i}. {trinket["name"]}, Amount in storage( not in use ): {trinket["details"]["amount"]}")
                    print(f"Effect: {tr.trinkets_info[trinket["name"]]["effect"]}")
                    print(f"Disassembly: {tr.trinkets_info[trinket["name"]]["disassembly"]}")
                    print()
            elif i % 5 == 0:
                if trinket["details"]["worn"] is not None:
                    print(f"{i}. {trinket["name"]}, Worn by: {trinket["details"]["worn"]}")
                    print(f"Effect: {tr.trinkets_info[trinket["name"]]["effect"]}")
                    print(f"Disassembly: {tr.trinkets_info[trinket["name"]]["disassembly"]}")
                    print()
                if trinket["details"]["amount"] is not None:
                    print(f"{i}. {trinket["name"]}, Amount in storage( not in use ): {trinket["details"]["amount"]}")
                    print(f"Effect: {tr.trinkets_info[trinket["name"]]["effect"]}")
                    print(f"Disassembly: {tr.trinkets_info[trinket["name"]]["disassembly"]}")
                    print()
                self.press_any_key()
                self.clear_screen()
            if i % 5 != 0 and i == len(trinkets_to_display):
                self.press_any_key()

    def manage_trinkets(self):
        loop = True
        while loop:
            self.clear_screen()
            print("1. Wear trinket")
            print("2. Remove all trinkets from all characters.")
            print("Q. Exit")
            answer = input(">>> ").lower()
            if answer == "1":
                inner_loop = True
                while inner_loop:
                    self.clear_screen()
                    for i, hero in enumerate(self.owned_heroes, start=1):
                        print(f"{i}.  {hero["name"]}, {hero["class"]}, Level: {hero["level"]},"
                              f" Weapon level: {hero["weapon lvl"]}, Armor level: {hero["armor lvl"]}, "
                              f"Worn trinkets: {hero["trinkets"]}")
                    print()
                    print("Choose hero to wear trinket")
                    ans = input("[Q for Exit.]>>> "). lower()
                    if ans == "q":
                        break
                    else:
                        try:
                            hero = self.owned_heroes[int(ans) - 1]
                            if len(hero["trinkets"]) < 2:
                                inner_inner_loop = True
                                while inner_inner_loop:
                                    self.clear_screen()
                                    counted = {}
                                    counted_list = []
                                    for element in owned_trinkets:
                                        counted[element] = owned_trinkets.count(element)
                                    for k, v in counted.items():
                                        counted_list.append({k: v})
                                    for i, element in enumerate(counted_list, start=1):
                                        for k, v in element.items():
                                            print(i, k, v)
                                    print()
                                    print(f"You have chosen {hero["name"]}. Trinkets: {hero["trinkets"]}")
                                    print("Please choose trinket to wear.")
                                    a = input("[Q for Exit.]>>> ")
                                    if a == "q":
                                        break
                                    elif a == "":
                                        pass
                                    else:
                                        if len(hero["trinkets"]) < 2:
                                            trinket = None
                                            for key in counted_list[int(a) - 1].keys():
                                                trinket = key
                                            self.wear_trinket(hero, trinket)
                                        if len(hero["trinkets"]) == 2:

                                            print(f"{hero["name"]} is worn 2 trinkets.\n{hero["trinkets"]}")
                                            self.press_any_key()
                                            break
                            else:
                                self.clear_screen()
                                print("The hero can't wear more than 2 trinkets.")
                                print(f"{hero["name"]} is already worn {hero["trinkets"]}")
                                self.press_any_key()

                        except IndexError:
                            self.clear_screen()
                            print("A hero with this number not exist.")
                            self.press_any_key()
                        except ValueError:
                            self.clear_screen()
                            print("Please provide some number instead of letters")
                            self.press_any_key()



                pass
            elif answer == "2":
                self.remove_all_trinkets()
            elif answer == "q":
                break
            else:
                pass


    def trinkets_storage(self):
        loop = True
        while loop:
            self.clear_screen()
            print("1. Show common trinkets.")
            print("2. Show rare trinkets.")
            print("3. Show unusual trinkets.")
            print("4. Show legendary trinkets.")
            print("Q. Exit.")
            answer = input(">>> ").lower()
            if answer == "1":
                self.display_trinkets("common")

            elif answer == "2":
                self.display_trinkets("rare")

            elif answer == "3":
                self.display_trinkets("unusual")
            elif answer == "4":
                self.display_trinkets("legendary")

            elif answer == "q":
                loop = False

    def menu(self):
        self.loop = True
        while self.loop:
            self.clear_screen()
            print(self.info)
            print("\n1. Trinket shop")
            print("2. Storage")
            print("3. Manage trinkets")
            print(f"4. {self.name} upgrade")
            print("Q. Exit")
            answer = input(">>> ").lower()
            if answer == "1":
                self.trinket_shop()
            elif answer == "2":
                self.trinkets_storage()
            elif answer == "3":
                self.manage_trinkets()
            elif answer == "4":
                self.enchant_menu()
            elif answer == "q":
                self.loop = False
            else:
                pass
