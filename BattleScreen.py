from PyUI.Screen import Screen
from TVPoke.BaseClasses.Trainer import Trainer
from PyUI.PageElements import *

class BattleScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (25, 255, 40))
        self.backGroundElements = [Image((50, 50), 100, 100, "./imgs/battleground.JPG")]
        self.selectTrainers=0
        self.goTo = ""

    def addTrainers(self, trainer1Poke, trainer2Poke):
        self.trainers = [
            Trainer(trainer1Poke, 1),
            Trainer(trainer2Poke, 2)
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
            self.elements.append(MoveButton((moveSpot[p]), move))
            p+=1



class MoveButton(Button):
    def __init__(self, pos, move):
        super().__init__(pos, 10, 10, move.name + " " + str(move.damage))
        self.move = move

    def onClick(self, screen):
        screen.trainers[1].pokemon[0].takeDamage(self.move)
        if screen.trainers[1].pokemon[0].hp <= 0:
            screen.trainers[1].pokemon.pop(0)
            if len(screen.trainers[1].pokemon) == 0:
                screen.trainers.pop(1)
                screen.goTo = "WIN"
        screen.trainers.reverse()
        #check if fainted, check if someone won, blah blah blah


        

                




