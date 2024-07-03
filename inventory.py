import random
import json
from items_list import items_to_drop
try:
    with open("player_inventory.json", mode='r') as file:
        data = json.load(file)
except FileNotFoundError:
    with open("player_inventory.json", mode="w") as file:
        json.dump({"Money": 0}, file, indent=2)
finally:
    with open("player_inventory.json", mode='r') as file:
        data = json.load(file)


class Inventory:
    def __init__(self):
        self.gold_amount = data["Money"]
        self.items_in_inventory = data
        self.items_list = items_to_drop

    def show_inventory(self):
        print(f"You have {self.gold_amount} gold.")
        for item in self.items_in_inventory.keys():
            if item == "Gold" or item == "Money":
                continue
            else:
                print(f"Item: {item},  "
                      f" Sell price: {self.items_in_inventory[item]["price"]},  "
                      f" Amount: {self.items_in_inventory[item]["amount"]}")

    def add_to_inventory(self):
        pass

    def get_drop(self):
        new_item = {}
        random_item = random.choice(list(self.items_list.keys()))
        print(random_item)
        if random_item == "Gold":
            self.gold_amount += self.items_list["Gold"]
            new_item["Money"] = self.gold_amount
        elif random_item in self.items_in_inventory.keys():
            x = self.items_in_inventory[random_item]["amount"]
            x += 1
            self.items_in_inventory[random_item] = {"price": self.items_list[random_item], "amount": x}
            new_item[random_item] = {"price": self.items_list[random_item], "amount": x}
        else:
            self.items_in_inventory[random_item] = {"price": self.items_list[random_item], "amount": 1}
            new_item[random_item] = {"price": self.items_list[random_item], "amount": 1}

        self.items_in_inventory.update(new_item)
        with open("player_inventory.json", mode="w") as file:
            json.dump(self.items_in_inventory, file, indent=2)


adams_inventory = Inventory()
adams_inventory.get_drop()


adams_inventory.show_inventory()






