from PyUI.Window import Window
##import the custom screens you made---
from SelectScreen import SelectScreen
from BattleScreen import BattleScreen
##-------------------------------------


window = Window("Example App", (0,255,0)) ##Create the window to work with

##Create Screen Objects for use------
selectScreen = SelectScreen(window)
battleScreen = BattleScreen(window)
##-----------------------------------

screen = selectScreen ##set screen to be the starting screen

while True: ##Game loop
    ##Enter code here to handle changes between screens---
    if selectScreen.state["goTo"] == "BATTLE":
        pokemonList1 = selectScreen.state["selectedPoke"][0]
        pokemonList2 = selectScreen.state["selectedPoke"][1]
        battleScreen.addTrainers(pokemonList1, pokemonList2)
        selectScreen.state["goTo"] = ""
        screen = battleScreen

    if screen == battleScreen:
        if screen.trainers[1].pokemon[0].hp <= 0:
            screen.trainers[1].pokemon.pop(0)
            if len(screen.trainers[1].pokemon) == 0:
                print("trainer 1 wins!")
                quit()
            if len(screen.trainers[0].pokemon) == 0:
                print("trainer 2 wins!")
                quit()
            screen.trainers.reverse()    




    ##----------------------------------------------------

    window.checkForInput(screen) #checks for inputs on the screen
    window.update(screen) #updates the window to reflect the new screen
