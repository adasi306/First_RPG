trinkets_info = {
    "Lucky Coin": {"effect": "+3% chance of critical hit.",
                   "disassembly": "1 Magical essence"},
    "Statue of the goddess of abundance": {"effect": "+1 HP when the hero consumes food.",
                                           "disassembly": "1 Magical essence"},
    "Leather bracelet": {"effect": "+1 point of armor.",
                         "disassembly": "1 Building part"},
    "Frying pan in good condition": {"effect": "+3% chance of critical hit.",
                                     "disassembly": "1 Mechanical part"},
    "A mothball full of herbs": {"effect": "+7 p.p. resistance to poisoning.",
                                 "disassembly": "1 Building part"},
    "Focusing lens": {"effect": "+5 p.p. chance to hit with hero's skill, +4% chance to hit critically.",
                      "disassembly": "1 Magical essence + 1 Mechanical part"},
    "Reinforcing almanac": {"effect": "Increases the attack statistic by 2 points. (adds 2 pts. when the attack value "
                            "is drawn).",
                            "disassembly": "2 Magical essences"},
    "Steel Carvasses": {"effect": "+2 points of armor",
                        "disassembly": "1 Mechanical part + 2 Building parts"},
    "Stone of life": {"effect": "+7 of the character's maximum HP ",
                      "disassembly": "2 Magical essences + 1 Building part"},
    "Jewel of the healers": {
        "effect": "+25% healing for skills used by the wearing character (healing is increased if"
        " the character\nuses the skill, but not if the character receives healing from someone else)",
        "disassembly": "2 Magical essences"},
    "Compass": {"effect": "+8 p.p. chance of being hit by a skill by the character",
                "disassembly": "2 Mechanical parts"},
    "Midaferratos hand statue": {"effect": "Treasures from battles and chests contain 20% more Ferrims.",
                                 "disassembly": "2 Building parts + 1 Magical essence"},
    "Collection of rare herbs": {"effect": "+35 p.p. resistance to poisoning, +25 p.p. resistance to stun, +15% healing "
                                 "from all sources.",
                                 "disassembly": "1 Magical essence + 2 Building parts"},
    "Lightning Power": {"effect": "+15 p.p. chance of critical hit.",
                        "disassembly": "2 Building parts + 2 Magical essences"},
    "Mechanical sound player": {"effect": "-30% stress points received.",
                                "disassembly": "2 Mechanical parts + 1 Building part"},
    "Night robe": {"effect": "+3 points to evasion (15 p.p.).",
                   "disassembly": "2 Magical essences + 2 Building parts"},
    "Egideon": {"effect": "+2 points of armor, + 2 points of speed, + 1 point chance of evasion, +5 points chance of"
                " \ncritical hit",
                "disassembly": "3 Building parts + 3 Magical essences + 1 Mechanical part"},
    "Banner of Theogorn": {
        "effect": "As long as the character wearing this banner is alive, any adventurer with less than"
        " 75%, deals \ndamage increased by 35%.",
        "disassembly": "4 Building parts + 3 Magical essences"},
    "Prototype counting machine": {"effect": "+ 20 p.p. chance to hit with hero's skill, +2 points chance to dodge.",
                                   "disassembly": "4 Mechanical parts"},
    "Bjorn's horn": {"effect": "During the first turn of the strike, all adventurers gain 6 pts of speed.",
                     "disassembly": "1 Building part + 3 Magical essences"}
}
trinkets_stats = {
    "Lucky Coin": {"rarity": "common", "stats": {"crit_chance": 3}, "disassembly": {"Magical essence": 1},
                   "cost": 250},
    "Statue of the goddess of abundance": {"rarity": "common", "stats": {}, "disassembly": {"Magical essence": 1},
                                           "cost": 300},
    "Leather bracelet": {"rarity": "common", "stats": {"armor": 1}, "disassembly": {"Building parts": 1},
                         "cost": 300},
    "Frying pan in good condition": {"rarity": "common", "stats": {"crit_chance": 3}, "disassembly": {"Mechanical parts": 1},
                                     "cost": 350},
    "A mothball full of herbs": {"rarity": "common", "stats": {"poison_resist": 7}, "disassembly": {"Building parts": 1},
                                 "cost": 250},
    "Focusing lens": {"rarity": "rare", "stats": {},
                      "disassembly": {"Magical essence": 1, "Mechanical parts": 1}, "cost": 750},
    "Reinforcing almanac": {"rarity": "rare", "stats": {"crit_chance": 4},
                            "disassembly": {"Magical essence": 2}, "cost": 900},
    "Steel Carvasses": {"rarity": "rare", "stats": {"armor": 2},
                        "disassembly": {"Mechanical parts": 1, "Building parts": 2}, "cost": 1000},
    "Stone of life": {"rarity": "rare", "stats": {"max health": 7},
                      "disassembly": {"Magical essence": 2, "Building parts": 1}, "cost": 700},
    "Jewel of the healers": {"rarity": "rare", "stats": {},
                             "disassembly": {"Magical essence": 2}, "cost": 800},
    "Compass":  {"rarity": "rare", "stats": {},
                 "disassembly": {"Mechanical parts": 2}, "cost": 900},
    "Midaferratos hand statue": {"rarity": "unusual", "stats": {},
                                 "disassembly": {"Magical essence": 1, "Building parts": 2}, "cost": 1800},
    "Collection of rare herbs": {"rarity": "unusual", "stats": {"poison_resist": 35, "stun_resist": 25},
                                 "disassembly": {"Magical essence": 1, "Building parts": 2}, "cost": 2000},
    "Lightning Power": {"rarity": "unusual", "stats": {"crit_chance": 15},
                                  "disassembly": {"Magical essence": 2, "Building parts": 2}, "cost": 1750},
    "Mechanical sound player": {"rarity": "unusual", "stats": {},
                                "disassembly": {"Mechanical parts": 2, "Building parts": 1}, "cost": 2000},
    "Night robe": {"rarity": "unusual", "stats": {"dodge": 3},
                   "disassembly": {"Magical essence": 2, "Building parts": 2}, "cost": 2500},
    "Egideon": {"rarity": "legendary", "stats": {"armor": 2, "speed": 2, "dodge": 1, "crit_chance": 5},
                "disassembly": {"Magical essence": 3, "Building parts": 3, "Mechanical parts": 1}, "cost": 2000},
    "Banner of Theogorn": {"rarity": "legendary", "stats": {},
                           "disassembly": {"Magical essence": 3, "Building parts": 4}, "cost": 2500},
    "Prototype counting machine": {"rarity": "legendary", "stats": {"dodge": 2},
                                   "disassembly": {"Mechanical parts": 4, "Building parts": 4}, "cost": 2500},
    "Bjorn's horn": {"rarity": "legendary", "stats": {"dodge": 2},
                     "disassembly": {"Magical essence": 3, "Building parts": 1}, "cost": 2250},
}
common_trinkets = ["Lucky Coin", "Statue of the goddess of abundance", "Leather bracelet",
                   "Frying pan in good condition", "A mothball full of herbs"]
rare_trinkets = ["Focusing lens", "Reinforcing almanac", "Steel Carvasses", "Stone of life",
                 "Jewel of the healers", "Compass"]
unusual_trinkets = ["Midaferratos hand statue", "Collection of rare herbs", "Lightning Power",
                    "Mechanical sound player", "Night robe"]
legendary_trinkets = ["Egideon", "Banner of Theogorn", "Prototype counting machine", "Bjorn's horn"]

trinkets = [common_trinkets, rare_trinkets, unusual_trinkets, legendary_trinkets]

# for key, value in trinkets_stats.items():
#     print(key)
#     for k, v in value.items():
#         print(k, v)
#     print()
# import random
# print()
# print("____ lets begin ____")
# tr_choice = random.choice(trinkets)
# print("list of trinkets : ", tr_choice)
# chosen_tr = random.choice(tr_choice)
# print("drawn trinket : ", chosen_tr)
#
# hero = {"name": "William",
#         "class": "Alchemist",
#         "level": 3,
#         "weapon lvl": 1,
#         "armor lvl": 3,
#         "exp": 0,
#         "trinkets": [],
#         "positive perks": {
#             "Willingness to live": "unlocked",
#             "Blessing": "unlocked"
#     },
#     "negative perks": {},
#     "stats": {
#         "attack min": 4,
#         "attack max": 5,
#         "max health": 31,
#         "armor": 2,
#         "dodge": 4,
#         "accuracy": 90,
#         "crit_chance": 7,
#         "speed": 3,
#         "stress": 0,
#         "status_effects": [],
#         "bleed_resist": 23,
#         "poison_resist": 35,
#         "stun_resist": 22
#         }
#     }
# print("Hero stats before :")
# print(hero["stats"])
#
# for stat, value in trinkets_stats[chosen_tr]["stats"].items():
#     print(stat, value)
#     hero["stats"][stat] += value
#
# print("Hero stats after :")
# print(hero["stats"])



