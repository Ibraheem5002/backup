from ursina import *
import time

class Loading(Entity):
    def __init__(self, gm):
        super().__init__()

        self.bg = Entity(
            parent=self,
            model="quad",
            texture=r"assets\bgs\load.png",
            scale=(8, 6),
            position=(0, 0, 2)
        )

        self.kn = Entity(
            parent=self,
            texture=r"assets\knight\run\sprite_0.png",
            model="quad",
            scale=(1.2, 1.3),
            position=(-3.5, -2.35, 0)
        )

        self.idx = 0
        self.gm = gm
        self.enabled = False
        self.animation_timer = 0
        self.is_complete = False

        self.run = [
            r"assets\knight\run\sprite_0.png",
            r"assets\knight\run\sprite_1.png",
            r"assets\knight\run\sprite_2.png",
            r"assets\knight\run\sprite_3.png",
            r"assets\knight\run\sprite_4.png",
            r"assets\knight\run\sprite_5.png",
            r"assets\knight\run\sprite_6.png",
        ]
    
    def on_enable(self):
        self.kn.x = -3.5
        self.animate_run()
    
    def animate_run(self,idx=0):
        if self.kn.X > 5:
            self.finish_loading()
            return
        
        self.kn.x += 0.2
        self.kn.texture = self.run[idx]
        idx = (idx + 1) % len(self.run)
        invoke(Func(self.animate_run,idx),delay=0.075)
    
    # def update(self):
    
    def finish_loading(self):
        self.gm.show_game()
        self.enabled = False