import random
class Agent:
    def __init__(self,name,health,sanity):
        self.name=name
        self.__hp=health
        self.__sp=sanity
    def hpeffect(self,effect):
        self.__hp+=effect
        print(f"{self.name} has gained {effect} health.")
    def speffect(self,effect):
        self.__sp+=effect
        print(f"{self.name} has gained {effect} sanity.")
    def status(self):
        print(f"{self.name}'s health is {self.__hp} and sanity is {self.__sp}.")
name=input("Name your agent. ")
health=random.randint(80,150)
Alive=True
Nugget=Agent(name,health,0)
while Alive==True:
    if Agent(Nugget.__sp)<=-45:
        print(f"{name} has distorted.")
        rand=random.randint(100,200)
        Agent.hpeffect(Nugget,rand)
        Agent.speffect(Nugget,45)
    if Agent.__hp<=0:
        Alive=False
        print(f"{name} has died.")

    Stage=(input("Continue on or pause. ")).lower()
    if Stage=="continue":
        event=1
        if event==1:
            print(f"{name} has encounter a abnormality.")
            action=(input("Fight or Flight ")).lower()
            if action=="fight":
                rand=random.randint(-1,-150)
                Agent.hpeffect(Nugget,rand)
            elif action=="flight":
                rand=random.randint(-1,-45)
                Agent.speffect(Nugget,rand)
            else:
                print("Command not understood.")
                Agent.hpeffect(Nugget,-100)
                Agent.speffect(Nugget,-25)
    else:
        print("You took a quick break.")
        Agent.status(Nugget)
