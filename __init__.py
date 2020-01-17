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
        self.name = name
        if not type(inventory) is Inventory:
            raise TypeError('py-rpg: inventory must be a dictionary!')
        for i in inventory:
            if not type(i) is Item:
                raise TypeError('py-rpg: starter_inv must contain an Item objects!')
        self.starter_inv = inventory

    def info(self):
        result = "Profession "+ self.name +" info\nStarter inventory:\n"
        result += "  Helmet: "+ self.starter_inv[helmet].name +"\n    Defense: "
        result += str(self.starter_inv[helmet].defense) +"\n    Speed: "
        result += str(self.starter_inv[helmet].speed) +"\n  Chestplate: "
        result += self.starter_inv[chestplate].name +"\n    Defense:"
NoProfession = PlayerProfession("No Profession",Inventory)

# Inventory & Items
class Inventory():
    pass

class Item():
    # Item base class.  Use for making your own items.
    pass

class EffectItem(Item):
    # An item that has an affect.
    # Create an EffectItemAttributes to create attributes for this item.
    def __init__(self, attributes):
        for key, 
class EffectItemAttributes():
    # Attributes object for EffectItem
    # For creating your own Attributes object please see the advanced section of the Wiki.
    pass

class WearableItem(Item):
    # An item that is marked as wearable.
    # Should only be used for creating new wearable items.
    # Should only be used in tandem with a new Inventory slot.
    pass
    
class Helmet(WearableItem):
    # An item that is wearable as a helmet.
    pass
class Chestplate(WearableItem):
    # An item that is wearable as a chestplate.
    pass
class Leggings(WearableItem):
    # An item that is wearable as leggings.
    pass
class Boots(WearableItem):
    # An item that is wearable as boots.
    pass


class Player():
    def __init__(self, name, p_class, profession):
        if not type(p_class) is PlayerClass:
            raise TypeError('py-rpg: p_class must be a PlayerClass type!')
        if not type(profession) is Profession:
            raise TypeError('py-rpg: profession must be a Profession type!')
        self.name = name
        self.max_hp = p_class.base_hp
        self.health = p_class.base_hp
        self.max_st = p_class.base_st
        self.stamina = p_class.base_st
        self.inventory = {}
        self.attack = p_class.base_atk
        self.defense = p_class.base_def
        self.speed = p_class.base_spd

    class Changes():
        # Used for making a changes object for a player's update function
        pass

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