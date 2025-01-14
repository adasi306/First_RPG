import json
import subprocess
import charakter_templates as ct
import trinkets as tr
import faker
import random

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

fk = faker.Faker()


class Shelter:
    def __init__(self):
        self.unlocked_perks = None
        self.probability_winner = None
        self.gold_req = None
        self.mat_req = None
        self.name = "Fallen City Shelter"
        self.city_list = data
        self.info = "\nWelcome after war.... long story.."
        self.gold = data_inventory["Money"]
        self.loop = True
        self.owned_heroes = owned_heroes
        self.amount_owned_heroes = len(owned_heroes)
        self.inventory = data_inventory
        self.materials = {"magical": 7, "mechanic": 1, "ordinary": 1}
        self.current_nr = None
        self.missing_element = None
        self.enchant_path2_info = None
        self.enchant_path1_info = None
        self.enchant_path2_req = None
        self.enchant_path1_req = None
        self.enchant_path2_level = None
        self.enchant_path1_level = None
        self.enchant_path2_name = None
        self.enchant_path1_name = None

    @staticmethod
    def clear_screen():
        subprocess.run('cls', shell=True)

    @staticmethod
    def press_any_key():
        print("\nPress Enter to continue ...")
        input()

    def wrong_number(self):
        self.clear_screen()
        print("Wrong character number... ")
        self.press_any_key()

    def show_owned_heroes(self):
        if self.owned_heroes:
            for i in range(len(self.owned_heroes)):
                print(f"{i + 1} . {self.owned_heroes[i]["name"]}, {self.owned_heroes[i]["class"]}, "
                      f"Level: {self.owned_heroes[i]["level"]}, Weapon level: {self.owned_heroes[i]["weapon lvl"]}, "
                      f"Armor level: {self.owned_heroes[i]["armor lvl"]}")
        else:
            print("You don't have any hero")

    def reload_inventory(self):
        with open("player_inventory.json", mode='r') as file5:
            data_inventory = json.load(file5)
            self.inventory = data_inventory
        return self.inventory
    
    def mat_gold_req(self, path_req, level):
        self.mat_req = {}
        self.gold_req = path_req[level + 1]["Money"]
        for key, value in path_req[level + 1]["Materials"].items():
            if value != 0:
                self.mat_req[key] = value

    def check_method(self, path_req, level):
        self.mat_gold_req(path_req, level)
        if self.mat_req:
            for name in self.mat_req:
                if self.mat_req[name] > self.inventory[name]:
                    print(f"You dont have enough {name}")
                    self.press_any_key()
                    return False

        if self.gold_req <= self.gold:
            return True
        else:
            print("You don't have enough gold")
            self.press_any_key()
            return False

    def save_enchanted_data(self, name, path, curr_encht_lvl):
        data[name][path]["level"] = curr_encht_lvl + 1
        data.update(data)
        with open("shelter_data.json", mode="w") as self.file:
            json.dump(data, self.file, indent=2)

    def mat_substr_inventory(self):
        self.gold -= self.gold_req
        self.inventory["Money"] -= self.gold_req
        for key, value in self.mat_req.items():
            self.inventory[key] -= value
        data_inventory.update(self.inventory)
        with open("player_inventory.json", mode="w") as file2:
            json.dump(data_inventory, file2, indent=2)

    def enchant_info(self,):
        self.clear_screen()
        print(f"Welcome at the {self.name}\n")
        print(f"Your {self.enchant_path1_name} is on level {self.enchant_path1_level}.  ")
        if self.enchant_path1_level >= len(self.enchant_path1_req):
            print("You gained max level.\n")
        else:
            self.mat_gold_req(self.enchant_path1_req, self.enchant_path1_level)
            owned_mat_info = []
            money = f"{data_inventory["Money"]} Ferrim "
            owned_mat_info.append(money)
            for k in self.mat_req.keys():
                owned_mat_info.append(f"{k} {data_inventory[k]}")
            print("Next level:")
            print(self.enchant_path1_info[self.enchant_path1_level + 1])
            print("You have :", owned_mat_info)
            print("")
        print(f"Your {self.enchant_path2_name} is on level {self.enchant_path2_level}.  ")
        if self.enchant_path2_level >= len(self.enchant_path2_req):
            print("You gained max level.\n")
        else:
            self.mat_gold_req(self.enchant_path2_req, self.enchant_path2_level)
            owned_mat_info = []
            money = f"{data_inventory["Money"]} Ferrim "
            owned_mat_info.append(money)
            for k in self.mat_req.keys():
                owned_mat_info.append(f"{k} {data_inventory[k]}")
            print("Next level:")
            print(self.enchant_path2_info[self.enchant_path2_level + 1])
            print("You have :", owned_mat_info)
            print("")

    def enchant_menu(self):
        inner_loop = True
        while inner_loop:
            self.enchant_info()
            print(f"\n1. Update {self.enchant_path1_name}")
            print(f"2. Update {self.enchant_path2_name}")
            print("Q. Exit")
            ans = input(">>> ").lower()

            if ans == "q":
                inner_loop = False
            elif ans == "1":
                try:
                    if self.enchant_path1_level < len(self.enchant_path1_req):
                        if self.check_method(self.enchant_path1_req, self.enchant_path1_level):
                            self.save_enchanted_data(self.name, "path1", self.enchant_path1_level)
                            self.mat_substr_inventory()
                            self.enchant_path1_level += 1
                    else:
                        self.clear_screen()
                        print("You already gain highest level !")
                        self.press_any_key()
                except ValueError:
                    print("Please enter the correct key")
            elif ans == "2":
                try:
                    if self.enchant_path2_level < len(self.enchant_path2_req):
                        if self.check_method(self.enchant_path2_req, self.enchant_path2_level):
                            self.save_enchanted_data(self.name, "path2", self.enchant_path1_level)
                            self.mat_substr_inventory()
                            self.enchant_path2_level += 1
                    else:
                        self.clear_screen()
                        print("You already gain highest level !")
                        self.press_any_key()
                except ValueError:
                    print("Please enter the correct key")
            else:
                pass

    @staticmethod
    def percentage_random_chance(percent):
        random_nr = random.randint(1, 100)
        return 1 <= random_nr <= percent

    def probability(self, a=0, b=0, c=0, d=0):
        win = [0, 1, 2, 3]
        weight = (a, b, c, d)
        winner = random.choices(win, weights=weight)
        self.probability_winner = winner[0]

    def new_perk_info(self, perk):
        self.clear_screen()
        print("Your hero get new perk.")
        print(perk)
        if perk in ct.positive_perks_info.keys():
            print(ct.positive_perks_info[perk])
        if perk in ct.negative_perks_info.keys():
            print(ct.negative_perks_info[perk])
        self.press_any_key()

    def check_lock_perk(self, perks_list):
        self.unlocked_perks = []
        for key, value in perks_list.items():
            if value == "unlocked":
                self.unlocked_perks.append(key)
        return self.unlocked_perks

    def adding_perk_stat(self, current_perk, current_hero, perk_stats):
        if current_perk in ct.perks_in_battle:
            pass
        elif current_perk == "Nasty sickness":
            for key in perk_stats[current_perk].keys():
                new_stat = (ct.negative_perks_stats[current_perk][key]["affected stat"])
                value = (ct.negative_perks_stats[current_perk][key]["value"])
                current_hero["stats"][new_stat] += value
        else:
            new_stat = perk_stats[current_perk]["affected stat"]
            value = perk_stats[current_perk]["value"]
            current_hero["stats"][new_stat] += value

    def substraction_perk_stat(self, current_perk, current_hero, perk_stats):
        if current_perk in ct.perks_in_battle:
            pass
        elif current_perk == "Nasty sickness":
            for key in perk_stats[current_perk].keys():
                new_stat = (ct.negative_perks_stats[current_perk][key]["affected stat"])
                value = (ct.negative_perks_stats[current_perk][key]["value"])
                current_hero["stats"][new_stat] -= value
        else:
            new_stat = perk_stats[current_perk]["affected stat"]
            value = perk_stats[current_perk]["value"]
            current_hero["stats"][new_stat] -= value

    def remove_perk(self, hero, perk):
        if perk in ct.positive_perks:
            self.substraction_perk_stat(perk, hero, ct.positive_perks_stat)
            del hero["positive perks"][perk]
        else:
            self.substraction_perk_stat(perk, hero, ct.negative_perks_stats)
            del hero["negative perks"][perk]

        with open("owned.json", mode="w") as file8:
            json.dump(self.owned_heroes, file8, indent=2)

    def add_perk(self, hero, chance):
        if self.percentage_random_chance(chance):
            drawn_list = ct.positive_perks
            char_perks = hero["positive perks"]
            stats = ct.positive_perks_stat
        else:
            drawn_list = ct.negative_perks
            char_perks = hero["negative perks"]
            stats = ct.negative_perks_stats
        perk = random.choice(drawn_list)
        while perk in char_perks.keys():
            perk = random.choice(drawn_list)
        if perk == "Weak head":
            if "Hard Head" in hero["positive perks"]:
                while perk == "Weak head":
                    perk = random.choice(drawn_list)
            else:
                pass
        if perk == "Hard Head":
            if "Weak head" in hero["negative perks"]:
                while perk == "Hard Head":
                    perk = random.choice(drawn_list)
            else:
                pass
        if len(char_perks) >= 5:
            self.check_lock_perk(char_perks)
            if self.unlocked_perks:
                perk_to_remove = random.choice(self.unlocked_perks)
                self.substraction_perk_stat(perk_to_remove, hero, stats)
                del char_perks[perk_to_remove]
                char_perks[perk] = "unlocked"
                self.adding_perk_stat(perk, hero, stats)
                return perk
            else:
                return ""
        else:
            char_perks[perk] = "unlocked"
            self.adding_perk_stat(perk, hero, stats)
            return perk

    def add_trinket_stats(self, hero, trinket):
        for stat, value in tr.trinkets_stats[trinket]["stats"].items():
            hero["stats"][stat] += value

    def wear_trinket(self, hero, trinket):
        if len(hero["trinkets"]) < 2:
            hero["trinkets"].append(trinket)
            self.add_trinket_stats(hero, trinket)
            with open("owned.json", mode="w") as file8:
                json.dump(self.owned_heroes, file8, indent=2)
            owned_trinkets.remove(trinket)
            with open("trinkets.json", mode="w") as file9:
                json.dump(owned_trinkets, file9, indent=2)
        else:
            self.clear_screen()
            print("You can not wear more than 2 trinkets")
            self.press_any_key()

    def sustract_trinket_stats(self, hero, trinket):
        for stat, value in tr.trinkets_stats[trinket]["stats"].items():
            hero["stats"][stat] -= value

    def un_wear_trinket(self, hero, trinket):
        self.sustract_trinket_stats(hero, trinket)
        hero["trinkets"].remove(trinket)
        with open("owned.json", mode="w") as file:
            json.dump(self.owned_heroes, file, indent=2)
        owned_trinkets.append(trinket)
        with open("trinkets.json", mode="w") as file7:
            json.dump(owned_trinkets, file7, indent=2)

    def remove_all_trinkets(self):
        self.clear_screen()
        print("Are you sure you want to remove all trinkets, from all characters [ Y/N ] ? ")
        answ = input(">>> ").lower()
        if answ == "y":
            for hero in owned_heroes:
                for trinket in hero["trinkets"][:]:
                    print(hero["name"], trinket)
                    self.un_wear_trinket(hero, trinket)
            print()
            print("All trinkets from all characters have been removed")
            self.press_any_key()
