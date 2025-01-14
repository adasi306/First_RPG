from shelter import Shelter
import charakter_templates as ct
import trinkets as tr
import json, faker
import random
from shelter import owned_heroes

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

# try:
#     with open("owned.json", mode='r') as file3:
#         owned_heroes = json.load(file3)
# except FileNotFoundError:
#     with open("owned.json", mode="w") as file3:
#         json.dump([], file3, indent=2)
# finally:
#     with open("owned.json", mode='r') as file3:
#         owned_heroes = json.load(file3)

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

class HeroesGuild(Shelter):
    def __init__(self):
        super().__init__()

        self.name = "Heroes Guild"
        self.enchant_path1_name = "Additional Character Slots"
        self.enchant_path2_name = "Better Selection"
        self.enchant_path1_req = ct.heroes_guild_p1_req
        self.enchant_path2_req = ct.heroes_guild_p2_req
        self.enchant_path1_info = ct.additional_slots_info
        self.enchant_path2_info = ct.better_selection_info
        self.enchant_path1_level = data["Heroes Guild"]["path1"]["level"]
        self.enchant_path2_level = data["Heroes Guild"]["path2"]["level"]

        self.gender_list = ['male', 'female']
        self.offered_hero = {}


        self.info = ("\nHi, you are alive, ... good. Many heroes would like to work for you. \n"
                     "Would you be willing to take a look . ")

    def unique_name(self):
        self.heros_name_list = []
        for i in range(len(self.owned_heroes)):
            self.heros_name_list.append(self.owned_heroes[i]["name"])
        if self.hero_name in self.heros_name_list:
            self.gender_and_name()
        else:
            self.heros_name_list.append(self.hero_name)

    def gender_and_name(self):
        gender = random.choice(self.gender_list)
        if gender == 'male':
            self.hero_name = fk.first_name_male()
            self.hero_gender = "male"
        else:
            self.hero_name = fk.first_name_female()
            self.hero_gender = "female"
        self.unique_name()

    def char_class_lottery(self):
        male_class = []
        female_class = []
        for char in ct.heroes_class_list:
            if char[5] == "male":
                male_class.append(char)
            else:
                female_class.append(char)
        if self.hero_gender == "male":
            self.char_class = random.choice(male_class)
        else:
            self.char_class = random.choice(female_class)

    def add_hero(self, nr):
        try:
            datas = self.offered_hero[nr]
            owned_heroes.append(datas)
            with open("owned.json", mode="w") as file:
                json.dump(owned_heroes, file, indent=2)
            self.offered_hero.pop(nr)
        except IndexError:
            self.wrong_number()

    def remove_hero(self):
        self.clear_screen()
        self.show_owned_heroes()
        if self.owned_heroes:
            try:
                ctr = input("\nWhich hero you want to remove [ Q for exit ] > ").lower()
                if ctr == "q":
                    pass
                else:
                    del owned_heroes[int(ctr) - 1]

                    with open("owned.json", mode="w") as file:
                        json.dump(owned_heroes, file, indent=2)
            except IndexError:
                self.wrong_number()
        else:
            pass

    def offered_heroes(self):
        while len(self.offered_hero) > 0:
            self.amount_owned_heroes = len(owned_heroes)
            available_space = ct.additional_slots[self.enchant_path1_level][1] - self.amount_owned_heroes
            if available_space > 0:
                pass
            else:
                self.clear_screen()
                print("Sorry, not enough space for new hero")
                self.press_any_key()
                break
            self.clear_screen()
            for _ in range(len(self.offered_hero)):
                hero = self.offered_hero[_]
                print(f"{_ + 1}. {hero["name"]}, {hero["class"]},"
                      f" 'Level':{hero["level"]},"                      
                      f"\nPositive perks: {hero["positive perks"]},"
                      f"\nNegative perks: {hero["negative perks"]}")
            print("\n")
            print(f"You can keep {available_space} heroes")
            answ = input("Which hero do you wish to keep ?\n[ Q. Exit ] >>> ").lower()
            if answ == "q":
                break
            else:
                try:
                    self.chosen_hero = int(answ)
                    self.add_hero(self.chosen_hero - 1)
                except ValueError:
                    self.wrong_number()
                finally:
                    pass

    def creating_heroes(self):
        self.reload_inventory()
        if self.inventory["Heroes Guild Token"] > 0:
            self.offered_hero = []
            self.number_of_slots = ct.additional_slots[self.enchant_path1_level][0]
            for i in range(self.number_of_slots):
                self.z = str(i + 1)
                self.gender_and_name()
                self.char_class_lottery()
                a = ct.better_selection[self.enchant_path2_level][0]
                b = ct.better_selection[self.enchant_path2_level][1]
                c = ct.better_selection[self.enchant_path2_level][2]
                d = ct.better_selection[self.enchant_path2_level][3]
                self.probability(a, b, c, d)
                stats = {}
                for _ in range(len(ct.template)):
                    stats[ct.template[_]] = self.char_class[self.probability_winner][_]

                offered_hero = {"name": self.hero_name, "class": self.char_class[6], "level": self.probability_winner + 1,
                                "weapon lvl": self.probability_winner + 1, "armor lvl": self.probability_winner + 1,
                                "exp": 0, "trinkets": [],
                                "positive perks": {}, "negative perks": {},
                                "stats": stats}
                for _ in range(ct.perks_amount[self.probability_winner]):
                    self.add_perk(offered_hero, 55)
                self.offered_hero.append(offered_hero)
            datas = {"Heroes Guild Token": 0}
            data_inventory.update(datas)
            with open("player_inventory.json", mode="w") as file2:
                json.dump(data_inventory, file2, indent=2)
            self.offered_heroes()
        else:
            self.offered_heroes()

    def worn_perks_info(self, hero):
        self.clear_screen()
        if hero["positive perks"]:
            print("Positive perks\n")
            for key in hero["positive perks"].keys():
                print(f"--{key}--")
                print(ct.positive_perks_info[key])
        if hero["negative perks"]:
            print("\nNegative perks\n")
            for key in hero["negative perks"].keys():
                print(f"--{key}--")
                print(ct.negative_perks_info[key])
        self.press_any_key()

    def show_hero_skills(self, hero):
        self.clear_screen()
        print(f"{hero["class"]:-^25}")
        for skill, info in ct.heroes_skills[hero["class"]].items():
            print(skill)
            print(info)
            self.press_any_key()

    def trinket_info(self, hero):
        self.clear_screen()
        if hero["trinkets"]:
            for trinket, info in tr.trinkets_info.items():
                for k in hero["trinkets"]:
                    if trinket == k:
                        print(trinket)
                        print(f"Effect: {info["effect"]}Disassembly: {info["disassembly"]}")
                        print()
            self.press_any_key()
        else:
            print(f"{hero["name"]} is not wearing any trinkets")
            self.press_any_key()

    def inspect_hero(self):
        inner_loop = True
        while inner_loop:
            self.clear_screen()
            self.show_owned_heroes()
            print("\nWhich hero do you wish to inspect?")
            answer = input("[ Q for exit ] >>> ").lower()
            if answer == "q":
                inner_loop = False
            else:
                inner_inner_loop = True
                while inner_inner_loop:
                    self.clear_screen()
                    hero = self.owned_heroes[int(answer) - 1]
                    print(f"{hero["name"]}, {hero["class"]}, Level: {hero["level"]}, Weapon level: {hero["weapon lvl"]}, "
                          f"Armor level: {hero["armor lvl"]}, Stress: {hero["stats"]["stress"]} ")
                    print(f"Offensive statistics: ")
                    print(f"Attack ({hero["stats"]["attack min"]}, {hero["stats"]["attack max"]}), "
                          f"Accuracy: {hero["stats"]["accuracy"]}, Crit chance: {hero["stats"]["crit_chance"]}, "
                          f"Speed: {hero["stats"]["speed"]}")
                    print(f"Defensive statistics: ")
                    print(f"Max HP: {hero["stats"]["max health"]}, Armor: {hero["stats"]["armor"]}, "
                          f"Dodge: {hero["stats"]["dodge"]}, Bleed resistance: {hero["stats"]["bleed_resist"]}, "
                          f"Poison resistance: {hero["stats"]["poison_resist"]}, "
                          f"Stun resistance: {hero["stats"]["stun_resist"]}")
                    print("\nPositive perks")
                    pos_perks = []
                    for key, value in hero["positive perks"].items():
                        text = f"{key}, status:{value}"
                        pos_perks.append(text)
                    print(pos_perks)
                    print("Negative perks")
                    neg_perks = []
                    for key in hero["negative perks"].keys():
                        neg_perks.append(key)
                    print(neg_perks)
                    print("Worn Trinket")
                    print(hero["trinkets"])
                    print("\n1 . Show skills ")
                    print("2 . Show perks info")
                    print("3 . Show trinkets info")
                    print("Q . Exit")
                    ans = input(">>> ").lower()
                    if ans == "1":
                        self.show_hero_skills(hero)
                    elif ans == "2":
                        self.worn_perks_info(hero)
                    elif ans == "3":
                        self.trinket_info(hero)
                    elif ans == "q":
                        break
                    else:
                        print("Please choose correct number")
                        pass

    def menu(self):
        self.loop = True
        while self.loop:
            self.clear_screen()
            print(self.info)
            print("\n1. Recruit hero")
            print("2. Manage owned heroes")
            print("3. Heroes Guild update")
            print("Q. Exit")
            answer = input(">>> ").lower()
            if answer == "1":
                self.creating_heroes()
            elif answer == "2":
                inner_loop = True
                while inner_loop:
                    self.clear_screen()
                    self.show_owned_heroes()
                    print("\n1 . Inspekt Hero")
                    print("2 . Remove Hero")
                    print("Q . Exit")
                    qa = input(">>> ").lower()
                    if qa == "1":
                        self.inspect_hero()
                    elif qa == "2":
                        self.remove_hero()
                    elif qa == "q":
                        inner_loop = False
                    else:
                        pass
            elif answer == "3":
                self.enchant_menu()
            elif answer == "q":
                self.loop = False
            else:
                pass
