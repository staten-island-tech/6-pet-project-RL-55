class Hero:
    def __init__(self,name,money,inventory,cost):
        self.name=name
        self.__money=money
        self.inventory=inventory
        self.cost=cost
    def buy(self,item,cost):
        self.inventory.append(item)
        self.cost+=cost
        print(self.inventory)
    def status(self):
        print(f"{self.name} has ${self.__money-self.cost} and {self.inventory}")
Nathan=Hero("Nahten",0,["Pencil"],0)
Hero.buy(Nathan,"nathan",999)
Hero.status(Nathan)

class BankAccount:
    def __init__(self,owner,balance):
        self.owner=owner
        self.__balance=balance
    def deposit(self,amount):
        self.__balance+=amount
    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")
#Nathan=BankAccount("Nathan",-100)
#BankAccount.showbalance(Nathan)

class Pet:
    def __init__(self, name, hp):
        self.name=name
        self.__happiness=hp
    def play(self,effect):
        self.__happiness+=effect
        print(f"{self.name} has gained {effect}.")
    def status(self):
        print(f"{self.name}'s happiness is now {self.__happiness}.")
#Dog=Pet("Sprinkles",20)
#Pet.play(Dog,30)
#Pet.status(Dog)