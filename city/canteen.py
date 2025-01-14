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


class Canteen(Shelter):
    def __init__(self):
        super().__init__()
        self.name = "Canteen"
        self.enchant_path1_name = "Better Assortment"
        self.enchant_path2_name = "Patronage"
        self.enchant_path1_req = ct.better_assort_req
        self.enchant_path2_req = ct.patronage_req
        self.enchant_path1_info = ct.better_assort_info
        self.enchant_path2_info = ct.patronage_info
        self.enchant_path1_level = data["Canteen"]["path1"]["level"]
        self.enchant_path2_level = data["Canteen"]["path2"]["level"]
        self.info = "\nOh, its you. don't get drunk like you did last time, and keep an eye on your people"

    def stress_reduction(self):
        pass

    def mini_games(self):
        pass

    def menu(self):
        self.loop = True
        while self.loop:
            self.clear_screen()
            print(self.info)
            print("\n1. Stress reduction. ")
            print("2. Mini games")
            print("3. Canteen upgrade")
            print("Q. Exit")
            answer = input("choose").lower()
            if answer == "1":
                self.stress_reduction()
            elif answer == "2":
                self.mini_games()

            elif answer == "3":
                self.enchant_menu()
            elif answer == "q":
                self.loop = False
            else:
                pass