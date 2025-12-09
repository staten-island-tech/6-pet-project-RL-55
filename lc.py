import random
class Agent:
    def __init__(self,name,health,sanity,enkephalin):
        self.name=name
        self.__ek=enkephalin
        self.__hp=health
        self.__sp=sanity
    def hpeffect(self,effect):
        self.__hp+=effect
        print(f"{self.name} health has changed by {effect}.")
    def speffect(self,effect):
        self.__sp+=effect
        if self.__sp>45:
            self.__sp=45
        print(f"{self.name} sanity has changed by {effect}.")  
    def ekeffect(self,effect):
        self.__ek+=effect
    def corrode(self):
        if self.__sp<=-45:
            self.__hp-=150
            print(f"{name} distorted. {name} has taken 150 damage.")
            self.__sp=0
    def status(self):
        print(f"{self.name}'s health is {self.__hp} and sanity is {self.__sp}.")
    def battle(self):
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
    def extraction(self):
        print(f"{name} is deployed to extract enkephalin.")
        action=(input("Work on ZAYIN, TENTH, HE, WAW, ALPH ")).lower()
        if action=="zayin":
            Agent.hpeffect(Nugget,-20)
            Agent.ekeffect(Nugget,1)
        elif action=="tenth":
            Agent.hpeffect(Nugget,-40)
            Agent.ekeffect(Nugget,2)
        elif action=="he":
            Agent.hpeffect(Nugget,-60)
            Agent.ekeffect(Nugget,5)
        elif action=="waw":
            Agent.hpeffect(Nugget,-80)
            Agent.ekeffect(Nugget,10)
        elif action=="alph":
            Agent.hpeffect(Nugget,-100)
            Agent.ekeffect(Nugget,25)
        else:
            print("Not understood ALPH selected.")
            Agent.hpeffect(Nugget,-100)
    def rest(self):
        print(f"{name} has a short break.")
        Agent.hpeffect(Nugget,50)
        Agent.speffect(Nugget,20)
    def egogear(self):
        print(f"{name} can now choose an E.G.O gear.")
        action=(input("Choose a ZAYIN, TENTH, HE, WAW, ALPH ")).lower()
        if action=="zayin":
            Agent.hpeffect(Nugget,20)
            Agent.speffect(Nugget,-10)
        elif action=="tenth":
            Agent.hpeffect(Nugget,40)
            Agent.speffect(Nugget,-20)
        elif action=="he":
            Agent.hpeffect(Nugget,60)
            Agent.speffect(Nugget,-30)
        elif action=="waw":
            Agent.hpeffect(Nugget,80)
            Agent.speffect(Nugget,-50)
        elif action=="alph":
            Agent.hpeffect(Nugget,100)
            Agent.speffect(Nugget,-75)
        else:
            print("Not understood ALPH selected.")
            Agent.hpeffect(Nugget,90)
            Agent.speffect(Nugget,-85)
    def spextraction(self):
        print(f"{name} is deployed to extract enkephalin.")
        action=(input("Work on ZAYIN, TENTH, HE, WAW, ALPH ")).lower()
        if action=="zayin":
            Agent.speffect(Nugget,-10)
            Agent.ekeffect(Nugget,1)
        elif action=="tenth":
            Agent.speffect(Nugget,-15)
            Agent.ekeffect(Nugget,2)
        elif action=="he":
            Agent.speffect(Nugget,-20)
            Agent.ekeffect(Nugget,5)
        elif action=="waw":
            Agent.speffect(Nugget,-30)
            Agent.ekeffect(Nugget,10)
        elif action=="alph":
            Agent.speffect(Nugget,-45)
            Agent.ekeffect(Nugget,25)
        else:
            print("Not understood ALPH selected.")
            Agent.speffect(Nugget,-45)
    def carmen(self):
        print(f"{name} hear a mysterious voice.")
        action=input((f"Does {name} listen or not? ")).lower
        if action=="listen":
            self.__hp-=150
            print(f"{name} distorted.,{name} has taken 150 damage.")
            self.__sp=0
        elif action=="don't" or action=="dont" or action=="no" or action=="not":
            print(f"{name} reinforced their resolve.")
            Agent.hpeffect(Nugget,self.__hp*2)
        else:
            print(f"{name} hides from the truth.")
            Agent.hpeffect(Nugget,self.__hp*2)
            Agent.speffect(Nugget,-45)
    def invite(self):
        action=(input(f"{name} has recieve a fancy invitation to a library. Accept or decline.")).lower
        if action=="accept":
            rand=random.randint(1,2)
            if rand==1:
                print(f"{name} has accepted the invitation.")
                Agent.hpeffect(Nugget,-999)
            else:
                print(f"{name} has decided not to go.")
        else:
            print(f"{name} refused the request.")
    def score(self):
        print(self.__ek)
    def play(self):
        day=1
        while self.__hp>0 and day<50:
            print(f"Day {day}")
            Stage=(input("Continue on or pause. ")).lower()
            if Stage=="continue" or Stage=="c" or Stage=="continue on":
                day+=1
                event=random.randint(1,37)
                if 10>=event>=1:
                    Agent.battle(Nugget)
                elif 21>=event>=11:
                    Agent.extraction(Nugget)
                elif 25>=event>=21:
                    Agent.rest(Nugget)
                elif 30>=event>=26:
                    Agent.egogear(Nugget)
                elif 40>=event>=31:
                    Agent.spextraction(Nugget)
                elif event==41:
                    Agent.carmen(Nugget)
                elif event==42:
                    Agent.invite(Nugget)
            else:
                print("You took a quick break.")
                Agent.status(Nugget)
            Agent.corrode(Nugget)
        if day>=50:
            print(f"{name}'s facility was engulfed by light.")
            Agent.score(Nugget)
        else:
            print(f"{name} has died.")
            Agent.score(Nugget)
name=input("Name your agent. ")
health=random.randint(80,150)
Nugget=Agent(name,health,0,0)
Agent.play(Nugget)