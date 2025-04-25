from PyUI.Screen import Screen
from PyUI.PageElements import *
from TVPoke.helper import getAllPokemonNames

class WinScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (4,50,3))


    def elementsToDisplay(self):
        self.elements = [ 
            Label((50, 50), 50, 10, "The winner is " + self.winner + "!", 24)
        ]

    
        
