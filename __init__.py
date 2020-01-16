class Class():
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

'''
class Profession():
    def __init__(self, name, base)
'''

class Player():
    def __init__(self, name, p_class):
        if not type(p_class) is Class:
            raise TypeError('py-rpg: p_class must be a PlayerClass type!')
        self.name = name
        self.max_hp = p_class.base_hp
        self.health = p_class.base_hp
        self.max_st = p_class.base_st
        self.stamina = p_class.base_st
        self.inventory = {}
        self.attack = p_class.base_atk
        self.defense = p_class.base_def
        self.speed = p_class.base_spd

    def update(self, changes):
        if isinstance(changes, dict): # Check if 'changes' is a dictionary.
            raise TypeError('\'changes\' should be a dictionary!')
        for key, value in changes.items():
            if key == "health":
                self.health += value
            elif key == "stanima":
                self.stamina += value
            elif key == "inventory":
                self.inventory[value[0]] == value[1]
            elif key == "speed":
                self.speed += value

            

#class Item():
#    def __init__(self):

#class Changes