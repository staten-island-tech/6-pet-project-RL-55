class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory
    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
Nathan=Hero("Nahten",0,["Pencil"])
Hero.buy(Nathan,"Slave")

class Pet:
    def __init__(self, name, happiness):
        self.name=name
        self.__happiness=happiness
    def play():
        
    def status():
