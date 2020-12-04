class BaseItem:
    """Basic item.

    Has no use other than possibly having a certian amount of uses, or durability, along with attack and defense stats.
    """

    def __init__(self, name:str, description:str, durability:int=-1, defense:int=0, attack:int=0) -> object:
        self.name = name
        self.desc = description
        self.dura = durability
        self.defs = defense
        self.atck = attack

    def use(self, dura_used:int=1):
        self.dura -= dura_used

class EffectItem(BaseItem):
    """Item that has an effect.
    
    Has additional properties: `effect`, `strength`, and `duration` each relating to the effect given by the item.
    """

    def __init__(self, name:str, description:str, effect:str="none", strength:int=1, length:int=1, durability:int=1) -> object:
        self.name = name
        self.desc = description
        self.efct = {}
        self.efct.efct = effect
        self.efct.strn = strength
        self.efct.leng = length
        self.dura = durability
