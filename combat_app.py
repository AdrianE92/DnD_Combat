from flask import Flask, render_template, request
from monster import create_monster, update_monster
import os
app = Flask(__name__)
"""
To implement:
- Initiative:
    - Order
- Monsters:
    - Create monster
    - Health
    - Skills
- Function for saving default
- ???
- Profit!
"""
path = "C:\\DnD_Combat\\monster_list"

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/combat", methods=['GET', 'POST'])
def combat():
    return render_template('combat.html')

@app.route("/monsters", methods=['GET', 'POST'])
def monsters():
    "Path to folder"
    "Create list of stored monsters"

    return render_template('monsters.html', mon_list=os.listdir(path))

@app.route("/new_monster", methods=['GET', 'POST'])
def new_monster():
    """
    monster = create_monster(request.form['name'], request.form['hp'], 
                             request.form['ac'], request.form['stats'], 
                             request.form['spells'], request.form['spell_slots'])

    """
    return render_template('new_monster.html')

@app.route("/cre_mon", methods=['GET', 'POST'])
def cre_mon():

    name = request.form.get("name")
    hp = request.form.get("hp")
    ac = request.form.get("ac")
    strength = request.form.get("str")
    dex = request.form.get("dex")
    con = request.form.get("con")
    intelligence = request.form.get("int")
    wis = request.form.get("wis")
    charisma = request.form.get("char")

    stats = {"strength": strength,
             "dex": dex,
             "con": con,
             "intelligence": intelligence,
             "wis": wis,
             "charisma": charisma}

    spells = {"Fireball": "Fireball Description",
              "Wall of Fire": "Wall of Fire Description",
              "Blink": "Blink Description"}

    spell_slots = 0
    monster = create_monster(name, hp, ac, stats, spells, spell_slots)
    if monster == 0:
        return render_template('monsters')
    else:
        #Create new monster
        f = open(os.path.join(path, (monster["Name"] + ".mon")), 'w')
        f.write(monster["Name"])
        f.write('\n')
        f.write("HP:" + monster["HP"])
        f.write('\n')
        f.write("Armor Class:" + str(monster["AC"]))
        f.write('\n')
        f.write("Stats: ")
        f.write('\n')
        for stat in monster["Stats"]:
            f.write(stat)
            f.write(str(monster["Stats"][stat]))
            f.write('\n')
        for spell in monster["Spells"]:
            f.write(spell)
            f.write(": ")
            f.write(monster["Spells"][spell])
            f.write("\n")
            
        f.write('\n')
        f.write(str(spell_slots)) 
        f.close()
            
    return render_template('monsters.html', mon_list=os.listdir(path))

@app.route("/help")
def help():
    return render_template('help.html')


if __name__ == '__main__':
    app.run(port=5001, debug=True)