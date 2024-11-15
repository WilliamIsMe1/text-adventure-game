class Item:
    def __init__(self, name, description, fixed=False):
        self.name = name
        self.description = description
        self.fixed = fixed
    def __str__(self):
        return "An item named: " + self.name

class Light(Item):
    def __init__(self, name, description, open_flame=True, fixed=False):
        self.name = name
        self.description = description
        self.fixed = fixed
        self.open_flame = open_flame

class Armor(Item):
    def __init__(self, name, description, ac = 10, fixed=False):
        self.name = name
        self.description = description
        self.fixed = fixed
        self.ac = ac

class Accessory(Item):
    def __init__(self, name, description, on_wear = None, fixed=False):
        self.name = name
        self.description = description
        self.fixed = fixed
        self.on_wear = on_wear if on_wear is not None else self.default_on_wear
    
    def default_on_wear(self):
        print("You have now equipped " + self.name)

class Inscription(Item):
    def __init__(self, name, description, fixed=False):
        self.name = name
        self.description = description
        self.fixed = fixed
        self.pages = []

    def add_page(self, words):
        self.pages.append(words)

    def remove_page(self, index):
        if 0 <= index < len(self.pages):
            return self.pages[index]
        self.pages.pop(index)
    
    def get_page(self, index):
        if 0 <= index < len(self.pages):
            return self.pages[index]

class Weapon(Item):
    def __init__(self, name, description, atk_mod=2, atk_dmg=6, fixed=False, ammo = None):
        self.name = name
        self.description = description
        self.atk_mod = atk_mod
        self.atk_dmg = atk_dmg
        self.fixed = fixed
        self.ammo = ammo

class Instrument(Item):
    def __init__(self, name, description, fixed=False):
        self.name = name
        self.description = description
        self.fixed = fixed

class Consumable(Item):
    def __init__(self, name, description, fixed=False):
        pass