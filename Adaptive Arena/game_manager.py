from menu import Mnu
from instructions import Inst
from game import Game
from loading import Loading
from ending import End

class GM:
    def __init__(self):
        self.menu = Mnu(self)
        self.inst = Inst(self)
        self.game = Game(self)
        self.load = Loading(self)
        self.end = End(self)
        self.status = None
    
    def show_menu(self):
        self.menu.enabled = True
        
        self.inst.enabled = False
        self.game.enabled = False
        self.load.enabled = False
        self.end.enabled = False
    
    def show_instructions(self):
        self.inst.enabled = True
        
        self.menu.enabled = False
        self.game.enabled = False
        self.load.enabled = False
        self.end.enabled = False
    
    def show_game(self):
        self.game.enabled = True
        self.game.reset_state()
        
        self.menu.exit_menu()
        self.load.enabled = False
        self.inst.enabled = False
        self.end.enabled = False
    
    def show_loading(self):
        self.load.enabled = True
        self.load.kn.x = -3.5  # Reset knight position
        
        self.game.enabled = False
        self.menu.exit_menu()
        self.inst.enabled = False
        self.end.enabled = False

    def show_end(self):
        self.end.enabled = True
        self.end.is_already_dead = False  # Reset state
        self.end.kn.x = -3.5  # Reset position
        
        self.game.enabled = False
        self.menu.exit_menu()
        self.inst.enabled = False
        self.load.enabled = False