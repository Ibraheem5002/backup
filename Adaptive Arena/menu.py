from ursina import *

class Mnu(Entity):
    def __init__(self, gm):
        super().__init__()

        self.bg = Entity(
            parent=self,
            model="quad",
            texture=r"assets\bgs\mnu.png",
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

        self.start_butt = Entity(
            parent=self,
            model='quad',
            texture=r"assets\ui\st_butt_1.png",
            scale=(1.4, 0.7),
            position=(0, -1.95, 0),
            collider='box'
        )

        self.inst_button = Entity(
            parent=self,
            model='quad',
            texture=r"assets\ui\inst_bt_1.png",
            scale=(3.85, 0.55),
            position=(0, -2.55, 0),
            collider='box'
        )

        self.msc = Audio(r'assets\music\menu_.mp3', autoplay=False, loop=True)

        self.enabled = False
        self.gm = gm
        self.bt_clicked = False
    
    def on_enable(self):
        if not self.msc.playing:
            self.msc.play()
    
    def exit_menu(self):
        self.msc.fade_out(duration=1)
        invoke(self.msc.stop, delay=1)
        self.enabled = False

    def update(self):
        if self.start_butt.hovered:
            self.start_butt.texture = r"assets\ui\st_butt_2.png"
            
            if mouse.left and not self.bt_clicked:
                self.bt_clicked = True
                self.gm.show_loading()
        else:
            self.start_butt.texture = r"assets\ui\st_butt_1.png"

        if self.inst_button.hovered:
            self.inst_button.texture = r"assets\ui\inst_bt_2.png"
            
            if mouse.left and not self.bt_clicked:
                self.bt_clicked = True
                self.gm.show_instructions()
        else:
            self.inst_button.texture = r"assets\ui\inst_bt_1.png"
        
        if not mouse.left:
            self.bt_clicked = False