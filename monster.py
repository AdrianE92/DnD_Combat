import os

def create_monster(name, hp, ac, stats, spells, spell_slots):
    """
    Params:
            name(str)
            hp(int)
            ac(int)
            stats(dict of str:int)
            spells(dict of str:str)
            spell_slots(dict of str:int)
    """
    if type(name) != str:
        print("Name must be a string")
        return ValueError

    monster = {"Name": name,
               "HP": hp,
               "AC": ac,
               "Stats": stats,
               "Spells": spells,
               "Spell_Slots": spell_slots}
    path = "C:\\DnD_Combat\\monster_list"
    
    if (monster["Name"] + ".mon") in os.listdir(path):
        print("works")  
        return 0
    
    return monster

def update_monster(monster, values):
    """
    Update values based on which is recieved
    """
    return monster

if __name__ == "__main__":
    values = {"Name", "HP", "AC", "Stats", "Spells", "Spell_Slots"}
    stats = {"strength": 1,
             "dex": 2,
             "con": 3,
             "intelligence": 4,
             "wis": 5,
             "charisma": 6}
    monster = create_monster("Hei", 5, 25, stats, {"One spell": "All spells"}, 0)
    #print((stat, monster["Stats"][stat]) for stat in monster["Stats"])
    """
    for stat in monster["Stats"]:
        print(stat, monster["Stats"][stat])
    monster2 = create_monster("Spellcaster", 10, 10, {"Fireball": "Fireball Description",
                                                  "Wall of Fire": "Wall of Fire Description",
                                                  "Blink": "Blink Description"}, 0)
    print(monster2["Spells"]["Blink"])
    print(monster["Spells"])
    """