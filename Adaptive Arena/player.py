from ursina import *

class Player(Entity):
    def __init__(self):
        super().__init__()
        self.enabled = False
        self.scale = (1.2,1.3)
        self.position = (-3.5,-0.75,0)
        self.model = "quad"
        self.texture = r"assets\knight\idle.png"

        self.health = 10
        self.charge = 0
        self.status = "idle"

        self.idle = r"assets\knight\idle.png"
        self.defend = r"assets\knight\defend.png"
        self.attack = [
            r"assets\knight\attack\sprite_0.png",
            r"assets\knight\attack\sprite_1.png",
            r"assets\knight\attack\sprite_2.png",
            r"assets\knight\attack\sprite_3.png",
            r"assets\knight\attack\sprite_4.png"
        ]
        self.dead = [
            r"assets\knight\dead\sprite_0.png",
            r"assets\knight\dead\sprite_1.png",
            r"assets\knight\dead\sprite_2.png",
            r"assets\knight\dead\sprite_3.png",
            r"assets\knight\dead\sprite_4.png",
            r"assets\knight\dead\sprite_5.png",
            r"assets\knight\dead\sprite_6.png",
        ]
        self.special = [
            r"assets\knight\special\sprite_0.png",
            r"assets\knight\special\sprite_1.png",
            r"assets\knight\special\sprite_2.png",
            r"assets\knight\special\sprite_3.png",
        ]
        self.run = [
            r"assets\knight\run\sprite_0.png",
            r"assets\knight\run\sprite_1.png",
            r"assets\knight\run\sprite_2.png",
            r"assets\knight\run\sprite_3.png",
            r"assets\knight\run\sprite_4.png",
            r"assets\knight\run\sprite_5.png",
            r"assets\knight\run\sprite_6.png",
        ]
    
    def animate_attack(self,idx=0):
        self.status = "attack"
        if idx >= len(self.attack):
            self.status = "idle"
            return

        self.texture = self.attack[idx]    
        invoke(Func(self.animate_attack,idx+1),delay=0.1)
    
    def animate_dead(self,idx=0):
        self.status = "dead"
        if idx >= len(self.dead):
            return
        
        self.texture = self.dead[idx]
        invoke(Func(self.animate_dead,idx+1),delay=0.1)
    
    def animate_special(self,idx=0):
        self.status = "special"
        if idx >= len(self.special):
            self.status = "idle"
            return

        self.texture = self.special[idx]
        invoke(Func(self.animate_special,idx+1),delay=0.1)
    
    def animate_defend(self,continue_=True):
        self.status = "defend"
        if continue_ == False:
            self.status = "idle"
            return
        
        self.texture = self.defend
        invoke(Func(self.animate_defend,not continue_),delay=1)
    
    def animate_run(self, idx=0):
        self.status = "run"
        if self.x >= -1:
            self.status = "idle"
            return
        
        self.x += 0.2
        self.texture = self.run[idx]
        idx = (idx + 1) % len(self.run)
        invoke(Func(self.animate_run, idx), delay=0.075)

    def animate_run1(self, idx=0):
        self.status = "run"
        if self.x >= 3.5:
            self.status = "idle"
            return

        self.x += 0.2
        self.texture = self.run[idx]
        idx = (idx + 1) % len(self.run)
        invoke(Func(self.animate_run1, idx), delay=0.075)

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
        self.position = (-3.5,-0.75,0)
        self.animate_run()