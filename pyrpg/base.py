# RPG Player
class Player():

    # RPG Player class.
    # Has a name, class and profession

    def __init__(self, name, p_class, p_profession):

        if not type(p_class) is PlayerClass:
            raise TypeError('py-rpg: p_class must be a PlayerClass type!')

        if not type(p_profession) is PlayerProfession:
            raise TypeError('py-rpg: profession must be a PlayerProfession type!')

        self.name = name
        self.max_hp = p_class.base_hp
        self.hp = p_class.base_hp
        self.max_st = p_class.base_st
        self.st = p_class.base_st
        self.inventory = p_profession.starter_inv
        self.attack = p_class.base_atk
        self.defense = p_class.base_def
        self.speed = p_class.base_spd

    def create_changes_dict(self, delta_hp, delta_st, delta_atk, delta_def, delta_spd):

        # Used for making a dictionary for a player's update function

        output = {}
        if not delta_hp == None:
            output["hp"] = delta_hp

        if not delta_st == None:
            output["st"] = delta_st

        if not delta_atk == None:
            output["atk"] = delta_atk

        if not delta_def == None:
            output["def"] = delta_def

        if not delta_spd == None:
            output["spd"] = delta_spd

        return output

    def update(self, changes):

        if type(changes) is dict: # Check if 'changes' is a dictionary.
            raise TypeError('\'changes\' should be a dictionary!')

        for key, value in changes.items():
            if key == "health":
                self.hp += value
            elif key == "stanima":
                self.st += value
            elif key == "inventory":
                self.inventory[value[0]] == value[1]
            elif key == "speed":
                self.speed += value


# Player Class
class PlayerClass():

    def __init__(self, name, health, stamina, attack, defense, speed):

        if not type(name) is str:
            raise TypeError('py-rpg: name must be an integer!')

        self.name = name
        
        if not type(health) is int:
            raise Exception('py-rpg: health must be an integer!')

        self.base_hp = health

        if not type(stamina) is int:
            raise TypeError('py-rpg: stamina must be an integer!')

        self.base_st = stamina

        if not type(attack) is int:
            raise TypeError('py-rpg: attack must be an integer!')

        self.base_atk = attack

        if not type(defense) is int:
            raise TypeError('py-rpg: defense must be an integer!')

        self.base_def = defense

        if not type(speed) is int:
            raise TypeError('py-rpg: speed must be an integer!')

        self.base_spd = speed


    def info(self):
        result = "Class '" + self.name + "' info\nBase Stats:\n  Health: "+str(self.base_hp)+"\n  Stamina: "
        result += str(self.base_st) +"\n  Attack: "+str(self.base_atk)+"\n  Defense: "
        result += str(self.base_def)+"\n  Speed: "+str(self.base_spd)
        return result

# Profession
class PlayerProfession():

    def __init__(self, name, inventory):
        if not type(name) is str:
            raise TypeError('py-rpg: name must be a string!')

        self.name = name
        if not type(inventory) is Inventory: # Check if inventory is an Inventory object
            raise TypeError('py-rpg: inventory must be an Inventory object!')
        
        self.starter_inv = inventory

    def info(self):
        result = "Profession "+ self.name +" info\nStarter inventory:\n"
        result += "  Helmet: "+ self.starter_inv.helmet.name +"\n    Defense: "
        result += str(self.starter_inv.helmet.defense) +"\n    Speed: "
        result += str(self.starter_inv.helmet.speed) +"\n  Chestplate: "
        result += self.starter_inv.chestplate.name +"\n    Defense:"
    

# Inventory & Items
class Inventory():
    def __init__(self, helmet, chestplate, leggings, boots, backpack, backpack_max):
        # Add another variable above to add another inventory slot.
        if not type(helmet) is Helmet:
            raise TypeError('py-rpg: helmet must be a Helmet object!')
        self.helmet = helmet

        if not type(chestplate) is Chestplate:
            raise TypeError('py-rpg: chestplate must be a Chestplate object!')
        self.chestplate = chestplate

        if not type(leggings) is Leggings:
            raise TypeError('py-rpg: leggings must be a Leggings object!')
        self.leggings = leggings

        if not type(boots) is Boots:
            raise TypeError('py-rpg: boots must be a Boots object!')
        self.boots = boots

        if not type(backpack) is list:
            raise TypeError('py-rpg: backpack must be a list!')
        if len(backpack) > backpack_max:
            raise ValueError('py-rpg: backpack cannot contain more items to start with!')
        for i in backpack:
            if not type(i) is Item:
                raise TypeError('py-rpg: backpack must only contain Item objects!')
            