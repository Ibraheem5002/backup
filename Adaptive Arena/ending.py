from ursina import *

class End(Entity):
    def __init__(self, gm):
        super().__init__()
        self.enabled = False

        self.bg = Entity(
            parent=self,
            model="quad",
            texture=r"assets\bgs\end.png",
            scale=(8, 4.5),
            position=(0, 0.75, 2)
        )
        self.flr = Entity(
            parent=self,
            model="quad",
            texture=r"assets\ui\floor.png",
            scale=(8, 1.5),
            position=(0, -2.25, 2)
        )
        self.kn = Entity(
            parent=self,
            model="quad",
            texture=r"assets\knight\run\sprite_0.png",
            scale=(1.2, 1.3),
            position=(-3.5, -0.85, 0)
        )
        self.text = Text(
            text='',
            font=r'assets\ui\Cinzel.ttf',
            color=color.black,
            position=(0, 0, 0),
            scale=2,
            origin=(0, 0)
        )
        self.mnu_bt = Entity(
            parent=self,
            model='quad',
            texture=r"assets\ui\bck_butt_1.png",
            scale=(1.4, 0.7),
            position=(0, -2.1, 0),
            collider='box'
        )
        self.msc = Audio(r"assets\music\end.mp3", autoplay=False, loop=True)

        self.gm = gm
        self.run_complete = False
        self.dead_complete = False
        self.poem_started = False

        self.run = [
            r"assets\knight\run\sprite_0.png",
            r"assets\knight\run\sprite_1.png",
            r"assets\knight\run\sprite_2.png",
            r"assets\knight\run\sprite_3.png",
            r"assets\knight\run\sprite_4.png",
            r"assets\knight\run\sprite_5.png",
            r"assets\knight\run\sprite_6.png",
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

        self.poem = [
            "All of this to die,",
            "so choose a life that's not dry,",
            "drop the script, the practiced lie,",
            "chase the self you kept hidden inside,",
            "live with open mind and eye,",
            "before the last and silent sigh."
        ]

        self.credits = [
            "Made By: Me",
            "Using Ursina, Python",
            "Sprites : Craftprix.net",
            "Background : Craftprix & Freepik",
            "Music : YT, soundimage.org & pixabay",
            "",
            "Thanks For Trying Out",
        ]
    
    def on_enable(self):
        self.kn.x = -3.5
        self.run_complete = False
        self.dead_complete = False
        self.poem_started = False
        self.text.text = ''
        self.msc.play()
        
        self.animate_run()
    
    def animate_run(self, idx=0):
        if self.kn.x >= -2:
            self.run_complete = True
            invoke(self.animate_dead,delay=0.5)
            return
        
        self.kn.texture = self.run[idx]
        self.kn.x += 0.2
        idx = (idx + 1) % len(self.run)
        invoke(Func(self.animate_run, idx), delay=0.1)
    
    def animate_dead(self, idx=0):
        if idx >= len(self.dead):
            self.dead_complete = True
            invoke(self.animate_poem,delay=0.5)
            return
        
        self.kn.texture = self.dead[idx]
        invoke(Func(self.animate_dead, idx+1), delay=0.5)
    
    def animate_poem(self, idx=0):
        if idx >= len(self.poem):
            invoke(self.animate_credits,delay=1)
            return

        self.text.text = self.poem[idx]
        invoke(Func(self.animate_poem, idx+1), delay=2.5)
    
    def animate_credits(self, idx=0):

        if idx >= len(self.credits):
            invoke(self.show_end_title, delay=2.5)
            return
        
        self.text.text = self.credits[idx]
        invoke(Func(self.animate_credits, idx+1), delay=2.5)
    
    def show_end_title(self):
        self.bg.texture = r"assets\bgs\end1.png"
        self.msc.fade_out(5)
        invoke(self.return_to_menu,delay=5)
    
    def go_to_menu(self):
        pass
    
    def return_to_menu(self):
        self.msc.fade_out(duration=1)
        invoke(self.msc.stop, delay=1)
        self.text.enabled = False
        self.gm.show_menu()
        self.enabled = False
    
    def update(self):
        if self.mnu_bt.hovered:
            self.mnu_bt.texture = r"assets\ui\bck_bt_2.png"

            if mouse.left:
                self.return_to_menu()
        else:
            self.mnu_bt.texture = r"assets\ui\bck_bt_1.png"