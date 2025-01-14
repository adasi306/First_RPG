import shelter
import json
import blacksmith, canteen, heroesguild, fortunetelling, infirmary, mausoleum, expedition


try:
    with open("player_inventory.json", mode='r') as file2:
        data_inventory = json.load(file2)
except FileNotFoundError:
    with open("player_inventory.json", mode="w") as file2:
        json.dump({"Money": 0}, file2, indent=2)
finally:
    with open("player_inventory.json", mode='r') as file2:
        data_inventory = json.load(file2)

shelter = shelter.Shelter()
blacksmith = blacksmith.Blacksmith()
canteen = canteen.Canteen()
heroes_guild = heroesguild.HeroesGuild()
fort_tel_chamber = fortunetelling.FortuneTellingChamber()
infirmary = infirmary.Infirmary()
mausoleum = mausoleum.Mausoleum()
expedition = expedition.Expedition()


def city():
    visit_shelter = True
    datas = {"Heroes Guild Token": 1, "Glittering Coin": 1}
    data_inventory.update(datas)
    with open("player_inventory.json", mode="w") as file6:
        json.dump(data_inventory, file6, indent=2)
    while visit_shelter:
        shelter.clear_screen()

        print(shelter.name)
        print(shelter.info)
        print("\nHere you can visit\n")
        print("1. Heroes Guild")
        print("2. Blacksmith")
        print("3. Canteen")
        print("4. Fortune Telling Chamber")
        print("5. Infirmary")
        print("6. Mausoleum")
        print("7. Expedition")
        print("Q. Exit")
        question = input("What do you want to do? [1/7] ").lower()

        if question == "1":
            heroes_guild.menu()
        elif question == "2":
            blacksmith.menu()
        elif question == "3":
            canteen.menu()
        elif question == "4":
            fort_tel_chamber.menu()
        elif question == "5":
            infirmary.menu()
        elif question == "6":
            mausoleum.menu()
        elif question == "7":
            expedition.menu()
        elif question == "q":
            visit_shelter = False
        else:
            print("You choose wrong number")


city()
