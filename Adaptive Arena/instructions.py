from ursina import *

class Inst(Entity):
    def __init__(self,gm):
        super().__init__()

        self.bg = Entity(
            parent=self,
            model="quad",
            texture=r"assets\bgs\help.png",
            scale=(8, 4.5),
            position=(0, 0.75, 2)
        )

        self.flr = Entity(
            parent=self,
            model="quad",
            texture=r"assets\ui\floor.png",
            scale=(8,1.5),
            position=(0,-2.25,2)
        )

        self.bck_butt = Entity(
            parent=self,
            model="quad",
            texture=r"assets\ui\bck_bt_1.png",
            scale=(1.4, 0.7),
            position=(0, -2.25, 0),
            collider='box'
        )

        self.gm = gm
        self.enabled = False

    def update(self):
        if self.bck_butt.hovered:
            self.bck_butt.texture = r"assets\ui\bck_bt_2.png"

            if mouse.left:
                self.gm.show_menu()
                
        else:
            self.bck_butt.texture = r"assets\ui\bck_bt_1.png"