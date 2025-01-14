from shelter import Shelter


class Expedition(Shelter):
    def __init__(self):
        super().__init__()
        self.info = "Welcome hero. Here you can prepare your expedition "

    def menu(self):
        loop = True
        while loop:
            self.clear_screen()
            print(self.info)
            print()
            print("please, select type of mission.")
            print()
            print("1. Discovery missions \nMissions to explore a specific percentage of all "
                  "“rooms” of the generated map.")
            print("2. Exploration missions \nMissions whose main goal is to find and interact with a specific number of"
                  "points/events scattered around \nthe map.")
            print("3. Boss missions \nThe goal of the mission is to find and kill a powerful enemy.")
            print("Q. exit")
            answer = input(">>> ").lower()
            if answer == "1":
                pass
            elif answer == "2":
                pass
            elif answer == "3":
                pass
            elif answer == "q":
                break
            else:
                pass
