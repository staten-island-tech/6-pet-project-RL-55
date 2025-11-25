import random
class Agent:
    def __init__(self,name,health,sanity):
        self.name=name
        self.__hp=health
        self.__sp=sanity
    def damage(self,effect):
        self.__hp-=effect
        print(f"{self.name} has take {effect} damage.")
    def spdamage(self,effect):
        self.__sp-=effect
        print(f"{self.name} has take {effect} sp damage.")
    def status(self):
        print(f"{self.name}'s health is{self.__hp} and sanity is{self.__sp}.")
name=input("Name your agent. ")
health=random.randint(80,150)
sanity=0
Alive=True
Nugget=Agent(name,health,sanity)
while Alive==True:
    event=1
    if event==1:
        print(f"{name} has encounter a abnormality.")
        action=(input("Fight or Flight ")).lower()
        if action=="fight":
            x=random.randint(1,150)
            Agent.damage(Nugget,x)
        elif action=="flight":
            Nugget.spdamage(name,random.randint(1,150))
        else:
            print("Command not understood.")
            Nugget.damage(name,80)
            Nugget.spdamage(name,25)

