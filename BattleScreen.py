from PyUI.Screen import Screen
from TVPoke.BaseClasses.Trainer import Trainer
from PyUI.PageElements import *

class BattleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (25, 255, 40))
        self.backGroundElements = [Image((50, 50), 100, 100, "./imgs/battleground.JPG")]
        self.selectTrainers=0

    def addTrainers(self, trainer1Poke, trainer2Poke):
        self.trainers = [
            Trainer(trainer1Poke),
            Trainer(trainer2Poke)
        ]
        
    def elementsToDisplay(self):
        self.elements = []
        self.elements.extend(self.backGroundElements)

        y = 10
        x = 20
        j=0
        p=0
        moveSpot=[(60,5),(60,15),(90,5),(90,15)]
        #two rows of three
        for trainer in self.trainers:
            poke = trainer.pokemon[0]
            if j < 1:    
                self.elements.append(Image((x, y), 20, 20, poke.img))
                self.elements.append(Label((x, y + 10), 20, 10, poke.name + " " + str(poke.hp)))
                j+=1
            else:
                self.elements.append(Image((x+55, y+40), 20, 20, poke.img))
                self.elements.append(Label((x+55, y+50), 20, 10, poke.name + " " + str(poke.hp)))
        
        for move in self.trainers[self.selectTrainers].pokemon[0].moves:
            moveNameDmgCrit = move.name + " " + str(move.damage) + " " + move.type
            self.elements.append(Label(moveSpot[p],10,10,moveNameDmgCrit))
            p+=1


        

                




