import random
class Agent:
    def __init__(self,name,health,sanity,enkephalin):
        self.name=name
        self.__ek=enkephalin
        self.__hp=health
        self.__sp=sanity
    def hpeffect(self,effect):
        self.__hp+=effect
        x=input(f"{self.name} health has changed by {effect}.")
    def speffect(self,effect):
        self.__sp+=effect
        if self.__sp>45:
            self.__sp=45
        x=input(f"{self.name} sanity has changed by {effect}.")  
    def ekeffect(self,effect):
        self.__ek+=effect
    def corrode(self):
        if self.__sp<=-45:
            self.__hp-=150
            x=input(f"{name} distorted. {name} has taken 150 damage.")
            self.__sp=0
    def status(self):
        x=input(f"{self.name}'s health is {self.__hp} and sanity is {self.__sp}.")
    def battle(self):
        x=input(f"{name} has to suppress a abnormality.")
        action=(input("Fight or Flight? ")).lower()
        if action=="fight":
            rand=random.randint(-150,-1)
            Agent.hpeffect(Nugget,rand)  
        elif action=="flight":
            rand=random.randint(-45,-1)
            Agent.speffect(Nugget,rand)
        else:
            x=input("Command not understood.")
            Agent.hpeffect(Nugget,-100)
            Agent.speffect(Nugget,-25)
    def extraction(self):
        x=input(f"{name} is deployed to extract enkephalin.")
        action=(input("Work on ZAYIN, TENTH, HE, WAW, ALPH: ")).lower()
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
            x=input("Not understood ALPH selected.")
            Agent.hpeffect(Nugget,-100)
    def rest(self):
        x=input(f"{name} has a short break.")
        Agent.hpeffect(Nugget,50)
        Agent.speffect(Nugget,20)
    def egogear(self):
        x=input(f"{name} can now choose an E.G.O gear.")
        action=(input("Choose a ZAYIN, TENTH, HE, WAW, ALPH: ")).lower()
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
        x=input(f"{name} is deployed to extract enkephalin.")
        action=(input("Work on ZAYIN, TENTH, HE, WAW, ALPH: ")).lower()
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
            x=input("Not understood. ALPH selected.")
            Agent.speffect(Nugget,-45)
    def c(self):
        x=input(f"{name} hear a mysterious voice.")
        action=input((f"Does {name} listen or not? ")).lower
        if action=="listen":
            self.__hp-=150
            x=input(f"{name} distorted.,{name} has taken 150 damage.")
            self.__sp=0
        elif action=="don't" or action=="dont" or action=="no" or action=="not":
            x=input(f"{name} reinforced their resolve.")
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
                x=input(f"{name} has accepted the invitation.")
                Agent.hpeffect(Nugget,-999)
            else:
                x=input(f"{name} has decided not to go.")
        else:
            x=input(f"{name} refused the request.")
    def kcorp(self):
        rand=random.randint(1,2)
        if rand==1:
            action=(input(f"{name} found a mysterious ample. What will {name} do? ")).lower
            if action=="accept" or action=="take" or action=="pick up":
                x=input(f"{name} injected the ample.")
                Agent.hpeffect(Nugget,100)
            else:
                x=input(f"{name} ignored the ample.")
        else:
            action=(input(f"{name} has found a mysterious vial. What will {name} do? ")).lower
            if action=="accept" or action=="take" or action=="pick up":
                x=input(f"{name} injected the vial.")
                Agent.hpeffect(Nugget,-100)
            else:
                x=input(f"{name} ignored the vail.")

    def score(self):
        print(self.__ek)
    def play(self):
        day=1
        x=input("Press enter to continue")
        x=input("Warning take notes")
        while self.__hp>0 and day<50:
            print(f"Day {day}")
            Stage=(input("Continue on or pause. ")).lower()
            if Stage=="continue" or Stage=="c" or Stage=="continue on":
                day+=1
                event=random.randint(1,45)
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
                elif 43>=event>=41:
                    Agent.kcorp
                elif event==44:
                    Agent.c(Nugget)
                elif event==45:
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