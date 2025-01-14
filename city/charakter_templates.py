template = ("attack min", "attack max", "max health", "armor", "dodge",
            "accuracy", "crit_chance", "speed", "stress", "status_effects",
            "bleed_resist", "poison_resist", "stun_resist")

offence_stats = {"attack min": 0, "attack max": 1, "accuracy": 5, "crit_chance": 6, "speed": 7}
defence_stats = {"max health": 2, "armor": 3, "dodge": 4, "bleed_resist": 10, "poison_resist": 11,
                 "stun_resist": 12}

mage_of_frenzy = [[3, 5, 18, 0, 2, 85, 7, 3, 0, [], 10, 10, 22],
                  [3, 6, 22, 0, 2, 90, 8, 4, 0, [], 12, 10, 25],
                  [4, 7, 25, 0, 3, 90, 9, 5, 0, [], 14, 10, 30],
                  [5, 7, 31, 1, 3, 95, 10, 6, 0, [], 16, 10, 35],
                  [6, 9, 35, 1, 3, 95, 12, 8, 0, [], 20, 10, 45],
                  'male', 'Mage Of Frenzy']
barbarian = [[5, 10, 30, 0, 0, 75, 10, 3, 0, [], 0, 0, 20],
             [6, 12, 37, 0, 0, 75, 13, 3, 0, [], 0, 0, 20],
             [7, 12, 43, 0, 0, 75, 17, 4, 0, [], 0, 0, 20],
             [7, 14, 49, 0, 0, 75, 21, 4, 0, [], 0, 0, 20],
             [8, 16, 55, 0, 0, 75, 25, 5, 0, [], 0, 0, 20],
             'male', 'Barbarian']
adventuress = [[7, 8, 20, 0, 5, 95, 10, 4, 0, [], 10, 20, 20],
               [8, 9, 23, 0, 5, 95, 13, 5, 0, [], 12, 24, 24],
               [8, 10, 27, 0, 6, 95, 15, 6, 0, [], 14, 28, 28],
               [10, 11, 31, 0, 6, 100, 17, 7, 0, [], 16, 32, 32],
               [11, 13, 35, 0, 7, 100, 20, 8, 0, [], 18, 36, 36],
               'female', 'Adventuress']
priestess = [[3, 6, 25, 1, 3, 100, 5, 2, 0, [], 10, 10, 20],
             [4, 7, 28, 1, 3, 100, 6, 2, 0, [], 12, 12, 24],
             [5, 8, 32, 1, 4, 100, 7, 3, 0, [], 14, 14, 28],
             [6, 9, 36, 2, 4, 100, 8, 3, 0, [], 16, 16, 32],
             [7, 10, 40, 2, 5, 100, 10, 4, 0, [], 18, 18, 36],
             'female', 'Priestess']
musketeer = [[4, 7, 25, 1, 3, 100, 10, 2, 0, [], 10, 10, 20],
             [5, 8, 28, 1, 3, 100, 13, 3, 0, [], 12, 12, 24],
             [6, 10, 32, 1, 4, 100, 17, 4, 0, [], 14, 14, 28],
             [7, 12, 36, 1, 4, 100, 21, 5, 0, [], 16, 16, 32],
             [8, 14, 40, 2, 5, 100, 25, 6, 0, [], 18, 18, 36],
             'female', 'Musketeer']
knight = [[3, 4, 30, 2, 0, 90, 5, 1, 0, [], 15, 15, 25],
          [4, 5, 35, 3, 0, 90, 5, 1, 0, [], 19, 19, 30],
          [5, 6, 40, 3, 0, 95, 5, 1, 0, [], 23, 23, 35],
          [6, 7, 45, 4, 0, 95, 5, 1, 0, [], 27, 27, 40],
          [7, 8, 50, 4, 0, 100, 10, 2, 0, [], 31, 31, 45],
          'male', 'Knight']
golem = [[6, 9, 60, 4, 1, 85, 7, 1, 0, [], 100, 20, 20],
         [7, 11, 70, 5, 1, 85, 8, 1, 0, [], 100, 30, 23],
         [9, 13, 90, 6, 2, 90, 9, 2, 0, [], 100, 40, 26],
         [10, 15, 110, 7, 2, 90, 10, 3, 0, [], 100, 50, 30],
         [10, 17, 125, 8, 2, 90, 12, 4, 0, [], 100, 60, 33],
         'male', 'Golem']
alchemist = [[4, 5, 22, 1, 3, 90, 7, 3, 0, [], 18, 30, 15],
             [5, 7, 26, 1, 3, 90, 8, 4, 0, [], 21, 30, 18],
             [7, 9, 31, 2, 4, 90, 9, 5, 0, [], 23, 35, 22],
             [8, 10, 34, 3, 5, 95, 10, 6, 0, [], 25, 40, 26],
             [10, 12, 40, 3, 6, 100, 12, 8, 0, [], 27, 50, 30],
             'male', 'Alchemist']
heroes_class_list = [mage_of_frenzy, barbarian, adventuress, priestess, musketeer,
                     knight, golem, alchemist]
heroes_class_dict = {'Mage Of Frenzy': mage_of_frenzy, 'Barbarian': barbarian,
                     'Adventuress': adventuress, 'Priestess': priestess, 'Golem': golem,
                     'Musketeer': musketeer, 'Knight': knight, 'Alchemist': alchemist}


positive_perks = ["Tough skin", "Good reflexes", "Lucky", "Strength", "Clot",
                  "Hard Head", "Calmness", "High blood clotting", "Determination",
                  "Iron will", "Proficient", "Collector", "Willingness to live",
                  "Blessing", "Team player"]
defence_perks = ("Tough skin", "Good reflexes", "Hard Head", "Vulnerability to poisoning",
                 "Weak head", "Thin skin", "Clumsiness", "Nasty sickness")
offence_perks = ("Lucky", "Strength", "Clot", "Proficient", "Poor eyesight")

positive_perks_stat = {"Tough skin": {"affected stat": "armor", "value": 1},
                       "Good reflexes": {"affected stat": "dodge", "value": 2},
                       "Lucky": {"affected stat": "crit_chance", "value": 4, "gambling chance": {"low": 10, "middle": 5,
                                                                                                 "high": 5}},
                       "Strength": {"affected stat": "attack max", "value": 1},
                       "Clot": {"affected stat": "attack min", "value": 1},
                       "Hard Head": {"affected stat": "stun_resist", "value": 10},
                       "Proficient": {"affected stat": "speed", "value": 1}}

positive_perks_info = {"Tough skin": "The character receives 1 point of armor.",
                       "Good reflexes": "The chance of dodging is increased by 2 pts. (10 p.p.)",
                       "Lucky": "The character's critical strike chance statistic is increased by 4 pts.\n"
                                "In addition, the chance of winning in the gambling den is increased\n"
                                "(-10% chance for the worst bracket and +5% each for the middle"
                                " and best brackets).",
                       "Strength": "Increases the character's maximum attack stat threshold by 1 \n"
                                   "(if the character has an attack level of 5-7,"
                                   " then with this perk he really has 5-8).",
                       "Clot": "Increases the hero's minimum attack stat threshold by 1 \n"
                               "(if the character has an attack at level 5-7,"
                               " then with this perk he really has 6-7)",
                       "Hard Head": "+10 p.p. stun resistance (cannot occur if the character "
                                    "already has the 'Weak Head' perk.\n- this attribute takes "
                                    "precedence if both perks are drawn at the same time,\n that is,"
                                    " the negative one is drawn)",
                       "Calmness": "The character receives 15% less stress points",
                       "High blood clotting": "The bleeding status decreases faster by 1 point per turn\n"
                                              "(e.g. If a character has 6 points of bleeding,"
                                              " he loses 4 points in the transition \nto the next turn, not 3 points,"
                                              " as if it were usual)",
                       "Determination": "If the character's current HP drops to half or lower then the character"
                                        " gets +5 pts \nto the chance of being hit and + 3 pts to the chance of"
                                        " dealing critical damage",
                       "Iron will": "Once per battle the character survives a situation in which he would lose his life",
                       "Proficient": "The character receives 1 point of speed",
                       "Collector": "The character finds an additional 20 % of Ferrim after winning a battle",
                       "Willingness to live": "Healing from all sources is increased by 15 %",
                       "Blessing": "Healing from all sources is increased by 25 %",
                       "Team player":  "As long as the character participates in the expedition,"
                                       " all effects that remove stress points are increased by 20 %"
                       }

negative_perks = ["Fragility", "Weak nerves", "Vulnerability to poisoning", "Fear of the enemy",
                  "Weak head", "Thin skin", "Gluttony", "Weak spirit", "Curse", "Stomach problems",
                  "Panic", "Fear of dying", "Poor eyesight", "Clumsiness", "Nasty sickness"]
negative_perks_stats = {"Vulnerability to poisoning": {"affected stat": "poison_resist", "value": -5},
                        "Weak head": {"affected stat": "stun_resist", "value": -10},
                        "Thin skin": {"affected stat": "bleed_resist", "value": -8},
                        "Poor eyesight": {"affected stat": "accuracy", "value": -5},
                        "Clumsiness": {"affected stat": "dodge", "value": -1},
                        "Nasty sickness": {1: {"affected stat": "bleed_resist", "value": -10},
                                           2: {"affected stat": "poison_resist", "value": -15},
                                           3: {"affected stat": "stun_resist", "value": -10}}}
negative_perks_info = {"Fragility": "The character receives damage increased by 10% (minimum 1 point of damage more)",
                       "Weak nerves": "The character receives 10% more stress points (minimum 1 stress point)",
                       "Vulnerability to poisoning": "The character receives -5 points of resistance to poisoning",
                       "Fear of the enemy": "The character receives 25% more stress points if in 1st position.",
                       "Weak head": "-10 p.p. resistance to stun (cannot occur if the character "
                                    "already has the “Hard head” perk).",
                       "Thin skin": "-8 p.p. resistance to bleeding",
                       "Gluttony": "Eating food reduces 2 p.p. of stress, but this is the only way a character "
                                   "can reduce stress \nduring an expedition (the effects of other characters'"
                                   " abilities do not reduce their stress either)",
                       "Weak spirit": "If the character is hit with a critical attack by an enemy then he receives "
                                      "an additional \n40% stress points",
                       "Curse": "Healing from all sources is reduced by 20%",
                       "Stomach problems": "The character does not receive the healing effect by eating food "
                                           "during the expedition",
                       "Panic": "If a character has 50 % or less HP, their accuracy drops by 15 points.",
                       "Fear of dying": "If a character's HP level drops below 25%, they receive 25% more stress points",
                       "Poor eyesight": "-5 p.p.chance of being hit by an opponent's skill",
                       "Clumsiness": "-1 dodge point",
                       "Nasty sickness": "Character receives - 10 % resistance to bleeding, -15 resistance to poisoning,"
                                         " -10 % resistance to stunning"
                       }
perks_in_battle = ["Calmness", "High blood clotting", "Determination", "Iron will",
                   "Collector", "Willingness to live", "Blessing", "Team player",
                   "Fragility", "Weak nerves", "Fear of the enemy", "Gluttony",
                   "Weak spirit", "Curse", "Stomach problems", "Panic", "Fear of dying"
                   ]


additional_slots = [[4, 10], [5, 10], [6, 12], [7, 12], [8, 15], [8, 20]]
better_selection = [[100, 0, 0, 0], [90, 10, 0, 0], [65, 20, 15, 0],
                    [65, 20, 15, 0], [35, 30, 25, 10], [35, 30, 25, 10]]
perks_amount = [2, 3, 4, 5]
perks_neg_to_pos = [0, 0, 0, 10, 10, 25]
blacksmith_p1 = (1, 0.9, 0.8, 0.65, 0.5)
blacksmith_p2 = (2, 3, 4, 5, 5)
eq_leveling_price = (50, 100, 125, 150)
better_shine = ([85, 15, 0, 0, 1], [65, 25, 10, 0, 1], [65, 25, 10, 0, 0.9],
                [50, 30, 15, 5, 0.9], [50, 30, 15, 5, 0.75], [30, 35, 20, 15, 0.75])
more_flash = (5, 6, 7, 8)
better_assort = ()
patronage = ()
higher_standards = ()

lower_price = ([1, 0], [0.9, 0], [0.7, 0], [0.5, 25])
regular = (0.25, )

additional_slots_info = {
    1: "Increases the number of characters to recruit from 4 to 5.\n"
       "Cost: 1250 Ferrim + 2 Building parts.",
    2: "Increases the number of characters to recruit from 5 to 6 and\n"
       "increases the maximum number of adventurers held to 12 seats.\n"
       "Cost: 1500 Ferrim + 3 Building parts.",
    3: "Increases the number of characters to recruit from 6 to 7.\n"
       "Cost: 2000 Ferrim + 5 Building parts.",
    4: "Increases the number of characters to recruit from 7 to 8 and\n"
       "increases the maximum number of adventurers held to 15 slots.\n"
       "Cost: 2000 Ferrim + 5 Building parts.",
    5: "Increases the number of slots in the Guild itself, making the limit of maintained\n"
       "adventurers increase to 20 seats.\n"
       "Cost: 2000 Ferrim + 5 Building parts."
}
better_selection_info = {
    1: "Gives a 10% chance that a new adventurer will have level II (level II equipments and 3 perks).\n"
       "Cost: 1500 Ferrim.",
    2: "Gives another 10% chance that the new adventurer will have level II (level II equipments and 3 perks) \n"
       "and 15% chance that the new adventurer will have level III (level III equipments and 4 perks).\n"
       "Cost: 2000 Ferrim.",
    3: "When a character appears in town, there is now a 10% chance that a negative perk will be changed\n"
       "to a random positive perk.\n"
       "Cost: 2000 Ferrim.",
    4: "Gives another 10% chance that a new adventurer will have level II (level II equipment and 3 perks) \n"
       "and another 10% chance that a new adventurer will have level III (level III equipment and 4 perks), \n"
       "and a 10% chance that a new adventurer will have level IV (level IV equipment and 5 perks).\n"
       "Cost: 3000 Ferrim.",
    5: "The chance to change a negative perk in each character is increased by 15%.\n"
       "Cost: 3500 Ferrim."
}
blacksmith_p1_info = {
    1: "Reduces the cost of upgrading equipment by 10%\n"
       "Cost: 2000 Ferrim + 3 Building parts.",
    2: "Reduces the cost of improving equipment by a further 10%\n"
       "Cost: 2500 Ferrim + 5 Building parts.",
    3: "Reduces the cost of improving equipment by a further 15%\n"
       "Cost: 3000 Ferrim + 3 Building parts + 3 Mechanical parts.",
    4: "Reduces the cost of improving equipment by another 15%.\n"
       "Cost: 3500 Ferrim + 3 Building parts + 5 Mechanical parts."
}

blacksmith_p2_info = {
    1: "Allows you to upgrade your character's equipment from level II to level III.\n"
       "Cost: 1000 Ferrim.",
    2: "Allows you to upgrade a character's equipment from level III to level IV.\n"
       "Cost: 1500 Ferrim + 3 Building parts + 1 Mechanical parts.",
    3: "Allows you to upgrade a character's equipment from level IV to level V.\n"
       "Cost: 2000 Ferrim + 5 Building parts + 5 Mechanical parts.",
    4: "2 times for each break between expeditions, the player can upgrade any of the character's equipment for free.\n"
       "Cost: 2500 Ferrim"
}

better_assort_info = {
    1: "Increases alcove stress reduction by 25%\n"
       "Cost: 500 Ferrim + 3 Building parts.",
    2: "Increases stress reduction in the pub by 30%\n"
       "Cost: 750F + 3 Building parts.",
    3: "Increases the chance of getting more stress reduction in the gambling games - 35% below 50 stress points and \n"
       "65% equally or above 50 stress points\n"
       "Cost: 1000 Ferrim + 3 Building parts +1 Mechanical parts.",
    4: "All form of rest reduce stress 15% more effectively\n"
       "Cost: 1000 Ferrim + 4 Building parts + 1 Mechanical parts.",
    5: "+10% chance of losing a negative perk while enjoying any form of rest \n"
       "Cost: 1500F + 5 Building parts + 2 Mechanical parts."
}

patronage_info = {
    1: "Increases the jackpot at the gambling games from 500F to 1000F (15% chance of drawing the 300F - 1000F range)\n"
       "Cost: 2000 Ferrim.",
    2: "Reduces the cost of a liquor rest from 75F to 55F\n"
       "Cost: 1500 Ferrim.",
    3: "One of the characters assigned to rest at gambling has 100% to bring a profit\n"
       "Cost: 3000 Ferrim.",
    4: "One of the resting places with liquor is always free\n"
       "Cost: 2000 Ferrim.",
    5: "Reduces the cost of all leisure activities by 20F\n"
       "Cost: 4000 Ferrim."
}

better_shine_info = {
    1: "Increases the chance of better glitter (after change: 65% for common, 25% for rare and 10% for unusual)\n"
       "Cost: 1000 Ferrim + 3 Magical essence.",
    2: "Reduces the price of all glitters by 10%\n"
       "Cost: 1000 Ferrim + 2 Magical essence + 2 Mechanical parts.",
    3: "Increases the chance of better glitter (after change: 50% for common, 30% for rare, \n"
       "15% for unusual and 5% for legendary)\n"
       "Cost: 1500 Ferrim + 6 Magical essence.",
    4: "Reduces the price of all glitters by a further 15%\n"
       "Cost: 2000 Ferrim + 3 Magical essence + 4 Mechanical parts.",
    5: "Increases the chance of better glitter (after change: 30% for common, 35% for rare, \n"
       "20% for unusual and 15% for legendary)\n"
       "Cost: 2000 Ferrim + 8 Magical essence."
}

more_flash_info = {
    1: "Adds another purchasable glitter (after buying this upgrade: 6)\n"
       "Cost: 750 Ferrim.",
    2: "Adds another purchasable glitter (after buying this upgrade: 7)\n"
       "Cost: 1200 Ferrim + 3 Building parts.",
    3: "Adds another purchasable glitter (after buying this upgrade: 8)\n"
       "Cost: 1500 Ferrim + 5 Building parts."
}

higher_standards_info = {
    1: "In addition to paid perk removal or fixation, there is a 15% chance to remove an additional negative perk\n"
       "for free (if the character has no additional negative perks then nothing happens)\n"
       "Cost: 2000 Ferrim + 3 Building parts + 2 Mechanical parts.",
    2: "In addition to healing or fixing the perk, the character also loses 20 stress points\n"
       "Cost: 1500Ferrim + 5 Building parts.",
    3: "The chance of removing an additional negative perk is increased by 10% and each visit of the character has a \n"
       "25% chance of giving a positive perk to the character titled 'Immunized' (if the character were to receive \n"
       "a negative perk there is a 40% chance that instead of a negative perk it would receive a positive perk).\n"
       "Cost: 2200 Ferrim + 4 Building parts  + 3 Mechanical parts + 1 Magical essence.",
}

lower_price_info = {
    1: "The cost of removing and fixing traits is reduced by 10%\n"
       "Cost: 1000 Ferrim + 3 Building parts + 1 Mechanical parts.",
    2: "The cost of removing and fixing features is reduced by 20%\n"
       "Cost: 1500 Ferrim + 3 Building parts + 2 Mechanical parts.",
    3: "The cost of removing and fixing traits is reduced by another 20%. On top of that, each character visit has \n"
       "25% to give a positive character trait entitled. “regular” (The cost of treatment is reduced by another 25%).\n"
       "Cost: 2500 Ferrim + 3 Mechanical parts."
}

heroes_guild_p1_req = {
    1: {"Money": 1250, "Materials": {"Building parts": 2, "Mechanical parts": 0, "Magical essence": 0}},
    2: {"Money": 1500, "Materials": {"Building parts": 3, "Mechanical parts": 0, "Magical essence": 0}},
    3: {"Money": 2000, "Materials": {"Building parts": 5, "Mechanical parts": 0, "Magical essence": 0}},
    4: {"Money": 2000, "Materials": {"Building parts": 5, "Mechanical parts": 0, "Magical essence": 0}},
    5: {"Money": 2000, "Materials": {"Building parts": 5, "Mechanical parts": 0, "Magical essence": 0}}}

heroes_guild_p2_req = {
    1: {"Money": 1500, "Materials": {"Building parts": 0, "Mechanical parts": 0, "Magical essence": 0}},
    2: {"Money": 2000, "Materials": {"Building parts": 0, "Mechanical parts": 0, "Magical essence": 0}},
    3: {"Money": 2000, "Materials": {"Building parts": 0, "Mechanical parts": 0, "Magical essence": 0}},
    4: {"Money": 3000, "Materials": {"Building parts": 0, "Mechanical parts": 0, "Magical essence": 0}},
    5: {"Money": 3500, "Materials": {"Building parts": 0, "Mechanical parts": 0, "Magical essence": 0}}}

blacksmith_p1_req = {
    1: {"Money": 2000, "Materials": {"Building parts": 3, "Mechanical parts": 0, "Magical essence": 0}},
    2: {"Money": 2500, "Materials": {"Building parts": 5, "Mechanical parts": 0, "Magical essence": 0}},
    3: {"Money": 3000, "Materials": {"Building parts": 3, "Mechanical parts": 3, "Magical essence": 0}},
    4: {"Money": 3500, "Materials": {"Building parts": 3, "Mechanical parts": 5, "Magical essence": 0}}
}

blacksmith_p2_req = {
    1: {"Money": 1000, "Materials": {"Building parts": 0, "Mechanical parts": 0, "Magical essence": 0}},
    2: {"Money": 1500, "Materials": {"Building parts": 3, "Mechanical parts": 1, "Magical essence": 0}},
    3: {"Money": 2000, "Materials": {"Building parts": 5, "Mechanical parts": 5, "Magical essence": 0}},
    4: {"Money": 2500, "Materials": {"Building parts": 5, "Mechanical parts": 0, "Magical essence": 0}}}

better_assort_req = {
    1: {"Money": 500, "Materials": {"Building parts": 3, "Mechanical parts": 0, "Magical essence": 0}},
    2: {"Money": 750, "Materials": {"Building parts": 3, "Mechanical parts": 0, "Magical essence": 0}},
    3: {"Money": 1000, "Materials": {"Building parts": 3, "Mechanical parts": 1, "Magical essence": 0}},
    4: {"Money": 1000, "Materials": {"Building parts": 4, "Mechanical parts": 1, "Magical essence": 0}},
    5: {"Money": 1500, "Materials": {"Building parts": 5, "Mechanical parts": 2, "Magical essence": 0}}}

patronage_req = {
    1: {"Money": 2000, "Materials": {"Building parts": 0, "Mechanical parts": 0, "Magical essence": 0}},
    2: {"Money": 1500, "Materials": {"Building parts": 0, "Mechanical parts": 0, "Magical essence": 0}},
    3: {"Money": 3000, "Materials": {"Building parts": 0, "Mechanical parts": 0, "Magical essence": 0}},
    4: {"Money": 2000, "Materials": {"Building parts": 0, "Mechanical parts": 0, "Magical essence": 0}},
    5: {"Money": 4000, "Materials": {"Building parts": 0, "Mechanical parts": 0, "Magical essence": 0}}}

better_shine_req = {
    1: {"Money": 1000, "Materials": {"Building parts": 0, "Mechanical parts": 0, "Magical essence": 3}},
    2: {"Money": 1000, "Materials": {"Building parts": 0, "Mechanical parts": 2, "Magical essence": 2}},
    3: {"Money": 1500, "Materials": {"Building parts": 0, "Mechanical parts": 0, "Magical essence": 6}},
    4: {"Money": 2000, "Materials": {"Building parts": 0, "Mechanical parts": 4, "Magical essence": 3}},
    5: {"Money": 2000, "Materials": {"Building parts": 0, "Mechanical parts": 0, "Magical essence": 8}}}

more_flash_req = {
    1: {"Money": 750, "Materials": {"Building parts": 0, "Mechanical parts": 0, "Magical essence": 0}},
    2: {"Money": 1200, "Materials": {"Building parts": 3, "Mechanical parts": 0, "Magical essence": 0}},
    3: {"Money": 1500, "Materials": {"Building parts": 5, "Mechanical parts": 0, "Magical essence": 0}}}

higher_standards_req = {
    1: {"Money": 2000, "Materials": {"Building parts": 3, "Mechanical parts": 2, "Magical essence": 0}},
    2: {"Money": 1500, "Materials": {"Building parts": 5, "Mechanical parts": 0, "Magical essence": 0}},
    3: {"Money": 2200, "Materials": {"Building parts": 4, "Mechanical parts": 3, "Magical essence": 1}}}

lower_price_req = {
    1: {"Money": 1000, "Materials": {"Building parts": 3, "Mechanical parts": 1, "Magical essence": 0}},
    2: {"Money": 1500, "Materials": {"Building parts": 3, "Mechanical parts": 2, "Magical essence": 0}},
    3: {"Money": 2500, "Materials": {"Building parts": 0, "Mechanical parts": 3, "Magical essence": 0}}}

mage_of_frenzy_skills = {
    "Fury": "An uncontrollable long dagger attack that is more dangerous the more the mage is "
            "exasperated. \nChance of additional strikes the higher the stress index is.\n"
            "Percentage of damage → 75%\n"
            "Percentage of hit → 70%\n"
            "Chance of critical hit →120%\n"
            "Position effect → □□■■ ●●●○ per selected field.\n"
            "Additional effects → cause bleeding (50% of maximum weapon damage),"
            " - 5 stress points for each \nadditional hit for the mage."
            "Each 20 points of stress gives a 17% chance that the character will make \nanother hit "
            "with this attack. The chance decreases as the stress is reduced with subsequent "
            "strikes.",
    "Trans": "The character uses the character's increasing stress to enhance his attack.\n"
             "Position effect → ■■■■ ○○○○ to one selected field.\n"
             "Imposes 10 points of stress on the target. The next skill used by the target will "
             "inflict 10% more \neffective for every 10 points of stress (only damage inflicted and "
             "healed is amplified). After the \ntarget performs the action (if it inflicted or "
             "healed damage), the character loses 13 stress points.",
    "Teasing": "The mage intensifies his frenzy by increasing his combat potential.\n"
               "Effect on positions → ■■■■ □□□□ on himself.\n"
               "Additional effects → Mage adds 30 stress points to himself + 20% of the stress "
               "points he already \nhas.",
    "Frenzied sweep": "A powerful attack with a metal gauntlet that has a chance to stun "
                      "the opponent.\n"
                      "Percentage of damage → 60%\n"
                      "Percentage of hit → 100%\n"
                      "Chance of critical hit →100%.\n"
                      "Position effect → □□■■ ●●○○ per selected field.\n"
                      "Additional effects → stun chance, + 10 stress points for the skill user",
                    }
barbarian_skills = {
    "Strike": "A powerful attack on a single opponent.\n"
              "Percentage of damage 100 %\n"
              "Percentage of hit - the hero's accuracy\n"
              "Critical hit chance - the hero's crit.\n"
              "Position effect → □□■■ ●●○○ per selected field.",
    "Broad cut": "A blow aimed at 2 adjacent opponents.\n"
                 "Percentage of damage 60 %\n"
                 "Percentage of hit - hero 's accuracy\n"
                 "Critical hit chance - hero's crit."
                 "Effect on positions → □□■■ ●●○○ on two adjacent fields.",
    "Stunning blow": "A powerful blow that can incapacitate the most powerful opponents - requires the "
                     "hero's hp below 25%\n"
                     "Percentage of damage 90%\n"
                     "Percentage of hit - hero's accuracy\n"
                     "Critical hit chance - hero's crit.\n"
                     "Position effect → □□■■ ●○○○○ per selected field.\n"
                     "Additional effects → Chance to stun.",
    "Battle Cry": "Damage buff 50% for 2 turns\n"
                  "Position effect → ■■■■ ○○○○ only on yourself"
                    }
adventuress_skills = {
    "Knife throwing": "A spectacular knife throw at a single opponent.\n"
                      "Percentage of damage 80%\n"
                      "Percentage of hit - accuracy of the hero\n"
                      "Critical hit chance of the hero's crit.\n"
                      "Position effect → □■■■□ ●●○○ per selected field.",
    "Angled blade": "Throws a poisoned blade that, when wounded, can poison an opponent.\n"
                    "Percentage of damage 50%\n"
                    "Percentage of hit - accuracy of the hero\n"
                    "Critical hit chance - the hero's crit.\n"
                    "Position effect → □■■■□ ○●●●● per selected field.\n"
                    "Additional effects → Chance to apply poison (50% max damage)",
    "A downpour of poisonous steel": "An attack to shower 2 adjacent enemy positions with poisonous "
                                     "arrows.An attack to shower 2 adjacent \nenemy positions with "
                                     "poisonous arrows.\n"
                                     "Percentage of damage 25%\n"
                                     "Hit percentage - 90% accuracy of the hero\n"
                                     "Critical hit chance - the hero's crit.\n"
                                     "Effect on positions → □■■□ ○●●●● on 2 adjacent fields.\n"
                                     "Additional effects → Chance to apply poison (40% max damage)",
    "Shadow Agility": "The character sharpens his senses, gaining incredible agility."
                      "Increases evasion stats by 2 points \nuntil the end of the fight\n"
                      "Position effect → ■■■■ ○○○○ only on yourself"
                      }
priestess_skills = {
    "Soothing touch": "A soothing prayer that can heal an ally's wounds.\n"
                      "Healing power - hero's damage\n"
                      "Critical hit chance - 50%\n"
                      "Effect on pos ■■■□ ○○○○ positions on selected ally.\n"
                      "Critical heals double the value",
    "Rise": "Healing the entire hero team.\n"
            "Percentage of damage 40% of damage.\n"
            "Critical hit chance - 40% on each hero separately.\n"
            "Effect on pos ■■■□ ○○○○ positions on the entire team.\n"
            "Critical heals double in value",
    "Blessing": "Incantation that causes the selected character to receive damage reduced by 50% for 2 turns.\n"
                "Effect on pos ■■□□□ ○○○○ positions on selected ally.",
    "Pax vobiscum": "Blessing that removes negative effects from 1 character.\n"
                    "Effect on pos ■■□□ ○○○○ positions per selected ally."
                    }
musketeer_skills = {
    "In the decimation": "Shot at one enemy in any position.\n"
                         "Percentage of damage - the hero's damage.\n"
                         "Percentage of hit - the hero's accuracy\n"
                         "Critical hit chance - the hero's crit.\n"
                         "Effect on positions ■□□□□ ●●●● to one selected field.",
    "Piercing shot": "A shot that pierces enemies precipitating momentum with each successive enemy penetrated and \n"
                     "applying bleeding to the last pierced enemy in which the bullet is lodged.\n"
                     "Percentage on damage 90% damage on the first character and - 35% on each subsequent character\n"
                     "Percentage of hit accuracy of the character\n"
                     "Critical hit chance of the hero's crit.\n"
                     "Effect on positions ■□□□□□ ●●●● from one target to a maximum of the entire opposing team.\n"
                     "Chance of statuses - bleeding (20% max damage)",
    "Splat": "Shot with paint marking the opponent's character for 2 turns.\n"
             "Percentage of damage 20% of the hero's damage.\n"
             "Percentage of hit accuracy of the hero\n"
             "Critical hit chance of the hero's crit.\n"
             "Effect on positions ■□□□□□ ●●●● on one selected field.\n"
             "Chance of statuses none - designation",
    "I have you at gunpoint": "Reduces the dodge of the selected opponent by 5 points for 2 turns.\n"
                              "Effect on pos ■□□□□ ●●●● for one selected field."
}
knight_skills = {
    "Strong stab": "A strong stab with a sword at one opponent.\n"
                   "Percentage from damage the hero's damage.\n"
                   "Percentage of hit the hero's accuracy\n"
                   "Critical hit chance of the hero's crit.\n"
                   "Effect on pos positions □□■■ ●●○○ per selected field.\n"
                   "Chance of statuses none",
    "Steel ribbon": "Lightning slash visible as a streak. The attack deals area damage and has an increased chance \nof "
                    "critical damage.\n"
                    "Percentage of damage 60% damage.\n"
                    "Percentage of hit accuracy of the hero\n"
                    "Critical hit chance - 2 x hero's crit.\n"
                    "Position effect □□■■ ●●○○○ on 2 adjacent fields.",
    "Amphibious strike": "A strong sword amphibious strike that can stun an enemy.\n"
                         "Percentage of damage 35% damage.\n"
                         "Percentage of hit the hero's accuracy\n"
                         "Critical hit chance of the hero's crit.\n"
                         "Effect on positions □□■■ ●●○○ per selected field.\n"
                         "Chance to stun statuses for 1 turn",
    "I am not afraid": "The character provokes attacks from all opponents on himself for 2 turns. During this time he\n"
                       "receives increased (by 2 points) armor (the effect does not overlap, but can be renewed). "
                       "The skill \ncannot be used if the character is in 2 positions further from the enemy.\n"
                       "Effect on positions □□■■ ○○○○ on self only.\n"
                       "Additional effects - Taunt for 2 turns + 2 points of armor."
}
golem_skills = {
    "Crushing": "A powerful melee attack using the golem's hard hands.\n"
                "Percentage on damage → 100%\n"
                "Percentage of hit → 80% of character's accuracy\n"
                "Critical hit chance →100%.\n"
                "Position effect → □□■■ ●●●○ per selected field.",
    "Essence Sucking": "An attack that draws life energy from living enemies, allowing the golem to regain vitality.\n"
                       "Percentage on damage → 40%\n"
                       "Hit percentage → 100% of the character's accuracy\n"
                       "Critical hit chance →100%.\n"
                       "Position effect → □□■■ ●○○○○ per selected field.\n"
                       "Additional effects - character heals by 100% of the damage dealt",
    "Strike": "Golem provokes opponents to focus their attacks on him.\n"
              "Position effect □□■■ ○○○○ only on itself.\n"
              "Additional effects - Taunt for 1 turn",
    "Energy release": "Golem releases some of accumulated energy in the form of a wave that deals damage to all "
                      "opponents.\n"
                      "Damage → 20% of the golem's max HP number distributed equally to each opponent\n"
                      "Hit percentage → 100% of the character's accuracy (on each opponent separately)\n"
                      "Critical hit chance → none\n"
                      "Position effect → □□■■ ●●●● damage distributed equally to each living opponent\n"
                      "Additional effects - user loses 20% of maximum HP points. If the character is on the Edge of "
                      "Death \nor using this skill would leave the character on the Edge of Death, the character "
                      "automatically \ndies, amplifying the skill's damage by an additional 10% of max HP."
}
alchemist_skills = {
    "Puncture": "A strong stab with a long knife, capable of leaving a bleeding wound.\n"
                "Percentage of damage → 80%\n"
                "Percentage of hit → 100% of character's accuracy\n"
                "Critical hit chance →100% of character's crit.\n"
                "Position effect → □■■■ ●●○○ per selected field.\n"
                "Additional effects - bleeding (50% max damage)",
    "Other uses": "The alchemist prepares his arsenal of potions and tools by changing the capabilities of some of \n"
                  "them, temporarily increasing the chance of being hit by an attack.\n"
                  "Position effect → ■■■■ ○○○○ only on himself\n"
                  "Additional effects - the alchemist gets +25% chance to hit for 1 turn with each attack and changes\n"
                  "the version of skills III and IV.",
    "A-Smoke Curtain / B-Dense Smoke": "A. - Smoke Curtain\n"
                                       "The character surrounds himself or an ally with a cloud of smoke.\n"
                                       "Position effect → ■■■■ ○○○○ on one target\n"
                                       "Additional effects - 5% chance to hit, + 5 points of evasion for 2 turns.\n"
                                       "B. - Dense smoke\n"
                                       "The alchemist throws a vial that, when shattered, creates a dense vapor that "
                                       "reduces the enemy's \naccuracy.\n"
                                       "Position effect → □■■■ ●●●○ per selected field.\n"
                                       "Additional effects - -50% accuracy",
    "A-Poisoning / B-Chemical marker": "A. - Poisoning\n"
                                       "Throws a projectile that creates toxic fumes when it hits a target.\n"
                                       "Positions effect → □■■■ ●●●○ to one selected field.\n"
                                       "Additional effects - imposes a poison effect (50% max damage)\n"
                                       "B. - Chemical marker\n"
                                       "Throws a vial which, when splashed, deals minor area damage but imposes a "
                                       "marker effect.\n"
                                       "Position effect → □■■■ ●●●○ on two adjacent fields.\n"
                                       "Additional effects - imposes a marking effect and reduces enemies' speed by 20%"
                                       " for 2 turns."

}
heroes_skills = {'Mage Of Frenzy': mage_of_frenzy_skills, 'Barbarian': barbarian_skills,
                 'Adventuress': adventuress_skills, 'Priestess': priestess_skills, 'Golem': golem_skills,
                 'Musketeer': musketeer_skills, 'Knight': knight_skills, 'Alchemist': alchemist_skills}