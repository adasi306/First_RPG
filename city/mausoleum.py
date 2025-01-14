from shelter import Shelter
import json


try:
    with open("fallen_heroes.json", mode='r') as file3:
        fallen_heroes = json.load(file3)
except FileNotFoundError:
    with open("fallen_heroes.json", mode="w") as file3:
        json.dump([], file3, indent=2)
finally:
    with open("fallen_heroes.json", mode='r') as file3:
        fallen_heroes = json.load(file3)


class Mausoleum(Shelter):
    def __init__(self):
        super().__init__()
        self.info = "R I P"
        self.z = 0

    def show_fallen_heroes(self, n=0):
        fallen_heroes.reverse()
        for i in range(n, len(fallen_heroes)):
            self.z = i + 1
            hero = fallen_heroes[i]
            print(f"{self.z}. {hero["name"]}, {hero["class"]}, Level: {hero["level"]}")
            if self.z % 10 == 0:
                break

    @staticmethod
    def dead_counter():
        how_many_dead = len(fallen_heroes)
        if how_many_dead == 0:
            print(f"This place is empty. You don't have any fallen hero")
        elif how_many_dead == 1:
            print(f"Here rests in peace {how_many_dead} hero")
        else:
            print(f"Here rests in peace {how_many_dead} heroes")
        return how_many_dead

    def show_hero_details(self, hero_id):
        try:
            if fallen_heroes:
                hero = fallen_heroes[hero_id]
                self.clear_screen()
                print(f"{hero["name"]}, {hero["class"]}, Level: {hero["level"]}, Weapon level: {hero["weapon lvl"]}, "
                      f"Armor level: {hero["armor lvl"]}\n")
                if hero["positive perks"]:
                    print("Positive perks")
                    pos_perks = []
                    for key, value in hero["positive perks"].items():
                        text = f"{key}, status:{value}"
                        pos_perks.append(text)
                    print(pos_perks)
                    print()
                if hero["negative perks"]:
                    print("Negative perks")
                    neg_perks = []
                    for key in hero["negative perks"].keys():
                        neg_perks.append(key)
                    if neg_perks:
                        print(neg_perks)
                        print()
                print(f"Offensive statistics: ")
                print(f"Attack ({hero["stats"]["attack min"]}, {hero["stats"]["attack max"]}), "
                      f"Accuracy: {hero["stats"]["accuracy"]}, Crit chance: {hero["stats"]["crit_chance"]}, "
                      f"Speed: {hero["stats"]["speed"]}")
                print()
                print(f"Defensive statistics: ")
                print(f"Max HP: {hero["stats"]["max health"]}, Armor: {hero["stats"]["armor"]}, "
                      f"Dodge: {hero["stats"]["dodge"]}, Bleed resistance: {hero["stats"]["bleed_resist"]}, "
                      f"Poison resistance: {hero["stats"]["poison_resist"]}, "
                      f"Stun resistance: {hero["stats"]["stun_resist"]}")
                self.press_any_key()
            else:
                print("Nobody dead yet.")
        except IndexError:
            self.clear_screen()
            print("A hero with this number is probably still among the living.")
            self.press_any_key()

    def menu(self):
        self.loop = True
        self.z = 0
        while self.loop:
            self.clear_screen()
            print(self.info)
            print("Here you can contemplate the fallen heroes.\n")
            people = self.dead_counter()
            print()
            if people > 0:
                print(f"1. Show fallen heroes.")
            print("Q. Exit")
            answer = input(">>> ").lower()
            if answer == "1" and people > 0:
                inner_loop = True
                while inner_loop:
                    self.clear_screen()
                    self.show_fallen_heroes(self.z)
                    print()
                    if people > 0:
                        print("1. Show hero details")
                    if people > 10:
                        print("2. Show next fallen heroes.")
                        print("3. Show previous fallen heroes.")
                    print("Q. Exit")
                    ans = input(">>>  ").lower()
                    if ans == "2" and people > 10:
                        pass
                    elif ans == "3" and people > 10:
                        if self.z == len(fallen_heroes):
                            self.z -= (self.z % 10) + 10
                        elif self.z == 10:
                            self.z -= 10
                        else:
                            self.z -= 20
                    elif ans == "1":
                        hero = input("Which hero detail would you like to see? >>> ")
                        try:
                            hero = int(hero) - 1
                            self.show_hero_details(hero)
                            if self.z == len(fallen_heroes):
                                self.z -= self.z % 10
                            else:
                                self.z -= 10
                        except ValueError:
                            self.clear_screen()
                            print("Please provide some number instead of letters")
                            self.press_any_key()
                            if self.z == len(fallen_heroes):
                                self.z -= self.z % 10
                            else:
                                self.z -= 10
                    elif ans == "q":
                        break
                    else:
                        if self.z == len(fallen_heroes):
                            self.z -= self.z % 10
                        else:
                            self.z -= 10
            if answer == "q":
                self.loop = False
            else:
                pass
