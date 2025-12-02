import random
Alive=True
class Agent:
    def __init__(self,name,health,sanity):
        self.name=name
        self.__hp=health
        self.__sp=sanity
    def hpeffect(self,effect):
        self.__hp+=effect
        print(f"{self.name} has {effect} health.")
    def speffect(self,effect):
        self.__sp+=effect
        if self.__sp>45:
            self.__sp=45
        print(f"{self.name} has {effect} sanity.")  
    def alive(self):
        if self.__sp<=-45:
            self.__hp-150
            print(f"{name} distorted.,{name} has taken 150 damage.")
        if self.__hp<=0:
            print(f"{name} has died.")
            return 
    def status(self):
        print(f"{self.name}'s health is {self.__hp} and sanity is {self.__sp}.")
    def play(self):
        while self.__hp>0:
            event=random.randint(1,10)
            Agent.alive(Nugget)
            Stage=(input("Continue on or pause. ")).lower()
            if Stage=="continue":
                event=1
                if event==1:
                    print(f"{name} has to suppress a abnormality.")
                    action=(input("Fight or Flight ")).lower()
                    if action=="fight":
                        rand=random.randint(-150,-1)
                        Agent.hpeffect(Nugget,rand)
                    elif action=="flight":
                        rand=random.randint(-45,-1)
                        Agent.speffect(Nugget,rand)
                    else:
                        print("Command not understood.")
                        Agent.hpeffect(Nugget,-100)
                        Agent.speffect(Nugget,-25)
                if event==2:
                    print(f"{name} is deployed to extract enkephalin.")
                    action=(input("Work on ZAYIN, TENTH, HE, WAW, ALPH ")).lower()
                    if action=="zayin":
                        Agent.hpeffect(Nugget,-20)
                    if action=="tenth":
                        Agent.hpeffect(Nugget,-40)
                    if action=="he":
                        Agent.hpeffect(Nugget,-60)
                    if action=="waw":
                        Agent.hpeffect(Nugget,-80)
                    if action=="alph":
                        Agent.hpeffect(Nugget,-100)
                    else:
                        print("Not understood ALPH selected.")
                        Agent.hpeffect(Nugget,-100)
                if event==3:
                    print(f"{name} has a short break.")
                    Agent.hpeffect(Nugget,50)
                    Agent.speffect(Nugget,20)
                if event==4:
                    print(f"{name} can now choose an E.G.O gear.")
                    action=(input("Choose a ZAYIN, TENTH, HE, WAW, ALPH ")).lower()
                    if action=="zayin":
                        Agent.hpeffect(Nugget,20)
                        Agent.speffect(Nugget,-10)
                    if action=="tenth":
                        Agent.hpeffect(Nugget,40)
                        Agent.speffect(Nugget,-20)
                    if action=="he":
                        Agent.hpeffect(Nugget,60)
                        Agent.speffect(Nugget,-30)
                    if action=="waw":
                        Agent.hpeffect(Nugget,80)
                        Agent.speffect(Nugget,-50)
                    if action=="alph":
                        Agent.hpeffect(Nugget,100)
                        Agent.speffect(Nugget,-75)
                    else:
                        print("Not understood ALPH selected.")
                        Agent.hpeffect(Nugget,90)
                        Agent.speffect(Nugget,-85)
            else:
                print("You took a quick break.")
                Agent.status(Nugget)
        Agent.alive(Nugget)

name=input("Name your agent. ")
health=random.randint(80,150)
Nugget=Agent(name,health,0)
Agent.play(Nugget)
