from ursina import *

class Enemy(Entity):
    def __init__(self):
        super().__init__()
        self.enabled = False
        self.scale = (1.2, 1.3)
        self.position = (1, -0.75, 0)
        self.model = "quad"
        self.texture = r"assets\skeleton\idle.png"

        self.health = 10
        self.charge = 0
        self.status = "idle"

        self.idle = None
        self.defend = None
        self.attack = []
        self.dead = []
        self.special = []

        self.load_skeleton()

    def animate_attack(self, idx=0):
        if idx >= len(self.attack):
            self.status = "idle"
            return

        self.texture = self.attack[idx]
        invoke(Func(self.animate_attack, idx+1), delay=0.25)

    def animate_dead(self, idx=0):
        if idx >= len(self.dead):
            return  # Stay dead
        
        self.texture = self.dead[idx]
        invoke(Func(self.animate_dead, idx+1), delay=0.25)
    
    def animate_special(self, idx=0):
        if idx >= len(self.special):
            self.status = "idle"
            return
        
        self.texture = self.special[idx]
        invoke(Func(self.animate_special, idx+1), delay=0.25)
    
    def animate_defend(self, continue_=True):
        if continue_ == False:
            self.status = "idle"
            return
        
        self.texture = self.defend
        invoke(Func(self.animate_defend, not continue_), delay=0.25)

    def animate(self):
        if self.status == "idle":
            self.texture = self.idle
    
    def update(self):
        self.animate()
        
    def reset_state(self):
        self.health = 10
        self.charge = 0
        self.status = "idle"
        self.enabled = True

    def load_fire(self):
        self.idle = r"assets\fire\idle.png"
        self.defend = r"assets\fire\defend.png"
        self.attack = [
            r"assets\fire\attack\sprite_0.png",
            r"assets\fire\attack\sprite_1.png",
            r"assets\fire\attack\sprite_2.png",
            r"assets\fire\attack\sprite_3.png",
            r"assets\fire\attack\sprite_4.png"
        ]
        self.dead = [
            r"assets\fire\dead\sprite_0.png",
            r"assets\fire\dead\sprite_1.png",
            r"assets\fire\dead\sprite_2.png",
            r"assets\fire\dead\sprite_3.png"
        ]
        self.special = [
            r"assets\fire\special\sprite_0.png",
            r"assets\fire\special\sprite_1.png",
            r"assets\fire\special\sprite_2.png",
            r"assets\fire\special\sprite_3.png",
        ]

    def load_gangster(self):
        self.idle = r"assets\gangster\idle.png"
        self.defend = r"assets\gangster\defend.png"
        self.attack = [
            r"assets\gangster\attack\sprite_0.png",
            r"assets\gangster\attack\sprite_1.png",
            r"assets\gangster\attack\sprite_2.png"
        ]
        self.dead = [
            r"assets\gangster\dead\sprite_0.png",
            r"assets\gangster\dead\sprite_1.png",
            r"assets\gangster\dead\sprite_2.png",
            r"assets\gangster\dead\sprite_3.png",
            r"assets\gangster\dead\sprite_4.png"
        ]
        self.special = [
            r"assets\gangster\special\sprite_0.png",
            r"assets\gangster\special\sprite_1.png",
            r"assets\gangster\special\sprite_2.png",
            r"assets\gangster\special\sprite_3.png",
        ]

    def load_minotaur(self):
        self.idle = r"assets\minotaur\idle.png"
        self.defend = r"assets\minotaur\defend.png"
        self.attack = [
            r"assets\minotaur\attack\sprite_0.png",
            r"assets\minotaur\attack\sprite_1.png",
            r"assets\minotaur\attack\sprite_2.png",
            r"assets\minotaur\attack\sprite_3.png"
        ]
        self.dead = [
            r"assets\minotaur\dead\sprite_0.png",
            r"assets\minotaur\dead\sprite_1.png",
            r"assets\minotaur\dead\sprite_2.png",
            r"assets\minotaur\dead\sprite_3.png",
            r"assets\minotaur\dead\sprite_4.png",
        ]
        self.special = [
            r"assets\minotaur\special\sprite_0.png",
            r"assets\minotaur\special\sprite_1.png",
            r"assets\minotaur\special\sprite_2.png",
            r"assets\minotaur\special\sprite_3.png",
        ]
        
    def load_skeleton(self):
        self.idle = r"assets\skeleton\idle.png"
        self.defend = r"assets\skeleton\defend.png"
        self.attack = [
            r"assets\skeleton\attack\sprite_0.png",
            r"assets\skeleton\attack\sprite_1.png",
            r"assets\skeleton\attack\sprite_2.png",
            r"assets\skeleton\attack\sprite_3.png",
        ]
        self.dead = [
            r"assets\skeleton\dead\sprite_0.png",
            r"assets\skeleton\dead\sprite_1.png",
            r"assets\skeleton\dead\sprite_2.png",
            r"assets\skeleton\dead\sprite_3.png",
        ]
        self.special = [
            r"assets\skeleton\special\sprite_0.png",
            r"assets\skeleton\special\sprite_1.png",
            r"assets\skeleton\special\sprite_2.png",
            r"assets\skeleton\special\sprite_3.png",
        ]
    
    def load_wizard(self):
        self.idle = r"assets\wizard\idle.png"
        self.defend = r"assets\wizard\defend.png"
        self.attack = [
            r"assets\wizard\attack\sprite_0.png",
            r"assets\wizard\attack\sprite_1.png",
            r"assets\wizard\attack\sprite_2.png",
            r"assets\wizard\attack\sprite_3.png",
        ]
        self.dead = [
            r"assets\wizard\dead\sprite_0.png",
            r"assets\wizard\dead\sprite_1.png",
            r"assets\wizard\dead\sprite_2.png",
            r"assets\wizard\dead\sprite_3.png",
        ]
        self.special = [
            r"assets\wizard\special\sprite_0.png",
            r"assets\wizard\special\sprite_1.png",
            r"assets\wizard\special\sprite_2.png",
            r"assets\wizard\special\sprite_3.png",
            r"assets\wizard\special\sprite_4.png",
            r"assets\wizard\special\sprite_5.png",
        ]