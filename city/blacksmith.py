from shelter import Shelter
import json
import charakter_templates as ct
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


class Blacksmith(Shelter):
    def __init__(self):
        super().__init__()
        self.name = "Blacksmith"
        self.enchant_path1_name = "Improved Production Technology"
        self.enchant_path2_name = "New Ways of Create Equipment"
        self.enchant_path1_req = ct.blacksmith_p1_req
        self.enchant_path2_req = ct.blacksmith_p2_req
        self.enchant_path1_info = ct.blacksmith_p1_info
        self.enchant_path2_info = ct.blacksmith_p2_info
        self.enchant_path1_level = data["Blacksmith"]["path1"]["level"]
        self.enchant_path2_level = data["Blacksmith"]["path2"]["level"]
        self.info = "\nHello adventurer, what do you need"

    def gear_upgrading(self, gear):
        if gear == "armor lvl":
            stats = ct.defence_stats
        else:
            stats = ct.offence_stats
        inner_loop = True
        while inner_loop:
            self.clear_screen()
            self.show_owned_heroes()
            p1_level = self.enchant_path1_level
            p2_level = self.enchant_path2_level
            print(f"\nPlease choose hero to upgrade {gear}.")
            ans = input("[ Q for exit ] >>> ").lower()
            if ans == "q":
                break
            else:
                try:
                    self.clear_screen()
                    hero = self.owned_heroes[int(ans) - 1]
                    hero_id = int(ans) - 1
                    print(f"{hero["name"]}, {hero["class"]}, "
                          f"Level: {hero["level"]}, Weapon level: {hero["weapon lvl"]}, "
                          f"Armor level: {hero["armor lvl"]}\n")
                    if ct.blacksmith_p2[p2_level] >= hero["level"] > hero[gear]:
                        stats_before = []
                        for key, value in hero["stats"].items():
                            if key in stats.keys():
                                stat = f"{key}: {value} "
                                stats_before.append(stat)
                        for key in hero["positive perks"].keys():
                            self.substraction_perk_stat(key, hero, ct.positive_perks_stat)
                        for key in hero["negative perks"].keys():
                            self.substraction_perk_stat(key, hero, ct.negative_perks_stats)
                        for trinket in hero["trinkets"]:
                            self.sustract_trinket_stats(hero, trinket)
                        stats_after = []
                        new_hero = hero
                        level = new_hero[gear]
                        clas = ct.heroes_class_dict[new_hero["class"]]
                        for k, v in stats.items():
                            new_hero["stats"][k] = clas[level][int(v)]
                        for key in new_hero["positive perks"].keys():
                            self.adding_perk_stat(key, new_hero, ct.positive_perks_stat)
                        for key in new_hero["negative perks"].keys():
                            self.adding_perk_stat(key, new_hero, ct.negative_perks_stats)
                        for trinket in hero["trinkets"]:
                            self.add_trinket_stats(new_hero, trinket)
                        for key, value in new_hero["stats"].items():
                            if key in stats.keys():
                                stat = f"{key}: {value} "
                                stats_after.append(stat)
                        upgrade_cost = round(ct.eq_leveling_price[hero[gear] - 1] * ct.blacksmith_p1[p1_level])
                        print(f"\nStatistics before upgrade\n{stats_before}\n"
                              f"Statistics after upgrade\n{stats_after}\n")
                        print(f"Upgrade cost {upgrade_cost} Ferrims. You have {self.gold} Ferrims\n")
                        print("1. Upgrade")
                        print("Q. Exit")
                        answ = input(">>> ").lower()
                        if answ == "1":
                            if self.gold >= upgrade_cost:
                                new_hero[gear] += 1
                                perk = self.add_perk(new_hero, 55)
                                if perk != "":
                                    self.new_perk_info(perk)
                                self.owned_heroes[hero_id] = new_hero
                                with open("owned.json", mode="w") as file3:
                                    json.dump(self.owned_heroes, file3, indent=2)
                                self.gold -= upgrade_cost
                                self.inventory["Money"] = self.gold
                                data_inventory.update(self.inventory)
                                with open("player_inventory.json", mode="w") as file2:
                                    json.dump(data_inventory, file2, indent=2)
                            else:
                                print("You don't have enough money. ")
                                self.press_any_key()
                        elif answ == "q":
                            pass
                        else:
                            pass
                    elif ct.blacksmith_p2[-1] == hero["level"] and hero["level"] == hero["armor lvl"]:
                        self.clear_screen()
                        print("You gained max lvl")
                        self.press_any_key()
                    elif ct.blacksmith_p2[p2_level] >= hero["level"] == hero["armor lvl"]:
                        self.clear_screen()
                        print("please work on the hero level")
                        self.press_any_key()
                except ValueError:
                    self.wrong_number()
                except IndexError:
                    self.wrong_number()

    def menu(self):
        self.loop = True
        while self.loop:
            self.clear_screen()
            print(self.info)
            print("\n1. Armor upgrading")
            print("2. Weapon upgrading")
            print("3. Blacksmith upgrading")
            print("Q. Exit\n")
            answer = input(">>> ").lower()
            if answer == "1":
                self.gear_upgrading("armor lvl")
            elif answer == "2":
                self.gear_upgrading("weapon lvl")

            elif answer == "3":
                self.enchant_menu()

            elif answer == "q":
                self.loop = False
            else:
                pass
