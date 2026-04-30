from ursina import *
import ui
import time
import random
from module import MarkovChains
from player import Player
from enemy import Enemy


class Game(Entity):
    def __init__(self, gm):
        super().__init__()
        self.enabled = False

        self.bg = Entity(
            parent=self,
            model="quad",
            scale=(8, 4.5),
            position=(0, 0.75, 2),
            texture=r"assets\dungeons\graveyard.png"
        )
        self.flr = Entity(
            parent=self,
            model="quad",
            texture=r"assets\ui\floor 2.png",
            scale=(8, 1.5),
            position=(0, -2.25, 2)
        )

        self.e_slain = Entity(
            parent=self,
            model="quad",
            texture=r"assets\ui\ENEMY SLAIN.png",
            scale=(5.4, 0.81),
            position=(0, 0, -1),
            enabled=False
        )
        self.u_died = Entity(
            parent=self,
            model="quad",
            texture=r"assets\ui\you died.png",
            scale=(5.4, 1),
            position=(0, 0, -1),
            enabled=False
        )

        self.atck_bt = Button(
            parent=self,
            texture=r"assets\ui\sword.png",
            color=color.white,
            scale=0.5,
            position=(-2.5, -1.9, 0),
            enabled=True,
            on_click=self.atck_pressed
        )
        self.dfnd_bt = Button(
            parent=self,
            texture=r"assets\ui\shield.png",
            color=color.white,
            scale=0.5,
            position=(-1.5, -1.9, 0),
            enabled=True,
            on_click=self.dfnd_pressed
        )
        self.chge_bt = Button(
            parent=self,
            texture=r"assets\ui\lightning.png",
            color=color.white,
            scale=0.5,
            position=(-2.5, -2.6, 0),
            enabled=True,
            on_click=self.chge_pressed
        )
        self.spcl_bt = Button(
            parent=self,
            texture=r"assets\ui\bomb.png",
            color=color.white,
            scale=0.5,
            position=(-1.5, -2.6, 0),
            enabled=False,
            on_click=self.spcl_pressed
        )

        self.msc = Audio(r'assets\music\graveyard.mp3', autoplay=False, loop=True)

        self.gm = gm
        self.module = MarkovChains()

        self.curr_lvl = 4
        self.in_op = None
        self.out_op = None

        self.show_special = False
        self.btn_is_pressed = False
        self.round_active = True

        self.pobj = Player()
        self.eobj = Enemy()

    # round n state check
    def reset_state(self):
        self.curr_lvl = 5
        self.round_active = True
        self.pobj.reset_state()
        self.eobj.reset_state()
        self.bg.texture = r"assets\dungeons\graveyard.png"
        self.eobj.load_skeleton()
        
        if self.msc:
            self.msc.stop()
        self.msc = Audio(r'assets\music\graveyard.mp3', autoplay=True, loop=True)

    def next_round(self):
        self.round_active = True
        self.curr_lvl += 1
        self.pobj.reset_state()
        self.eobj.reset_state()
        
        if self.msc:
            self.msc.fade_out(duration=0.5)
            invoke(self.msc.stop, delay=0.5)

        if self.curr_lvl == 2:
            self.bg.texture = r"assets\dungeons\volcano.png"
            self.eobj.load_fire()
            self.msc = Audio(r'assets\music\volcano_.mp3', autoplay=True, loop=True)

        elif self.curr_lvl == 3:
            self.bg.texture = r"assets\dungeons\forest.png"
            self.eobj.load_wizard()
            self.msc = Audio(r'assets\music\forest_.mp3', autoplay=True, loop=True)

        elif self.curr_lvl == 4:
            self.bg.texture = r"assets\dungeons\terrace.png"
            self.eobj.load_minotaur()
            self.msc = Audio(r'assets\music\terrace.mp3', autoplay=True, loop=True)

        elif self.curr_lvl == 5:
            self.bg.texture = r"assets\dungeons\london.png"
            self.eobj.load_gangster()
            self.msc = Audio(r'assets\music\london.mp3', autoplay=True, loop=True)

    def check_state(self):
        if not self.round_active:
            return

        if self.eobj.health <= 0:
            self.round_active = False
            invoke(self.p_won, delay=2)

        if self.pobj.health <= 0:
            self.round_active = False
            self.e_won()

    # end graphics
    def show_u_died(self):
        self.u_died.enabled = True

    def show_e_slain(self):
        self.e_slain.enabled = True

    def p_won(self):
        self.eobj.status = "dead"
        self.eobj.animate_dead()
        invoke(self.show_e_slain, delay=1)
        invoke(self.go_to_next_round, delay=3)

    def e_won(self):
        self.pobj.status = "dead"
        self.pobj.animate_dead()
        invoke(self.show_u_died, delay=1)
        invoke(self.return_to_menu, delay=3)

    def go_to_next_round(self):
        self.e_slain.enabled = False
        self.msc.fade_out(duration=1)

        if self.curr_lvl <= 4:
            self.pobj.status = "run"
            self.pobj.animate_run1()
            invoke(self.next_round, delay=1.5)
        else:
            self.gm.show_end()
            self.pobj.enabled = False
            self.eobj.enabled = False
            ui.hide()
            self.enabled = False

    def return_to_menu(self):
        self.msc.fade_out(duration=1)
        invoke(self.msc.stop, delay=1)
        self.u_died.enabled = False
        ui.hide()
        self.pobj.enabled = False
        self.eobj.enabled = False
        self.curr_lvl = 1
        self.gm.show_menu()
        self.enabled = False

    # special check
    def spcl_ready(self):
        if self.pobj.charge >= 5:
            self.spcl_bt.enabled = True
        else:
            self.spcl_bt.enabled = False

    def get_out_move(self):
        X = random.randint(0, 100)

        if X <= 60 and self.eobj.charge >= 5:
            self.out_op = "S"
        else:
            # self.out_op = self.module.predict(self.in_op, self.curr_lvl)
            self.out_op = "C" # test
            print(f"\nEnemy chose: {self.out_op}")

    # p n e actions
    def p_do_attack(self):
        self.eobj.health -= 1
        self.pobj.status = "attack"
        self.pobj.animate_attack()

    def e_do_attack(self):
        self.pobj.health -= 1
        self.eobj.status = "attack"
        self.eobj.animate_attack()

    def both_do_attack(self):
        self.pobj.status = "attack"
        self.eobj.status = "attack"
        self.pobj.animate_attack()
        self.eobj.animate_attack()

    def p_do_charge(self):
        if self.pobj.charge < 5:
            self.pobj.charge += 1

    def e_do_charge(self):
        if self.eobj.charge < 5:
            self.eobj.charge += 1

    def p_do_defend(self):
        self.pobj.status = "defend"
        self.pobj.animate_defend()

    def e_do_defend(self):
        self.eobj.status = "defend"
        self.eobj.animate_defend()

    def p_do_special(self):
        self.eobj.health -= 5
        self.pobj.charge = 0
        self.pobj.status = "special"
        self.pobj.animate_special()

    def e_do_special(self):
        self.pobj.health -= 5
        self.eobj.charge = 0
        self.eobj.status = "special"
        self.eobj.animate_special()

    # handle buttons
    def atck_pressed(self):
        if not self.round_active:
            return
            
        self.btn_is_pressed = True
        self.in_op = "A"

        self.dfnd_bt.enabled = False
        self.chge_bt.enabled = False
        self.spcl_bt.enabled = False

        self.handle_turn()
        return True

    def dfnd_pressed(self):
        if not self.round_active:
            return
            
        self.btn_is_pressed = True
        self.in_op = "D"

        self.atck_bt.enabled = False
        self.chge_bt.enabled = False
        self.spcl_bt.enabled = False

        self.handle_turn()
        return True

    def chge_pressed(self):
        if not self.round_active:
            return
            
        self.btn_is_pressed = True
        self.in_op = "C"

        self.atck_bt.enabled = False
        self.dfnd_bt.enabled = False
        self.spcl_bt.enabled = False

        self.handle_turn()
        return True

    def spcl_pressed(self):
        if not self.round_active:
            return
            
        self.btn_is_pressed = True
        self.in_op = "S"

        self.atck_bt.enabled = False
        self.dfnd_bt.enabled = False
        self.chge_bt.enabled = False

        self.handle_turn()
        return True

    def reset_btn(self):
        self.atck_bt.enabled = True
        self.dfnd_bt.enabled = True
        self.chge_bt.enabled = True
        self.spcl_ready()

    # turn return
    def do_moves(self):
        if self.in_op == "A":
            if self.out_op == "C":
                self.p_do_attack()
            elif self.out_op == "D":
                self.e_do_defend()
            elif self.out_op == "A":
                self.both_do_attack()
            return

        if self.out_op == "A":
            if self.in_op == "C":
                self.e_do_attack()
            elif self.in_op == "D":
                self.p_do_defend()
            return
        
        if self.in_op == "D" and self.out_op == "D":
            self.p_do_defend()
            self.e_do_defend()
            return
        
        if self.in_op == "D" and self.out_op == "C":
            self.p_do_defend()
            self.e_do_charge()
            return
        
        if self.in_op == "C" and self.out_op == "D":
            self.p_do_charge()
            self.e_do_defend()
            return
        
        if self.in_op == "C" and self.out_op == "C":
            self.p_do_charge()
            self.e_do_charge()

    def handle_turn(self):
        if self.in_op == "S":
            self.p_do_special()
        else:
            self.get_out_move()

            if self.out_op == "S":
                self.e_do_special()
            else:
                self.do_moves()

        invoke(self.reset_btn, delay=0.5)

    # game loop
    def update(self):
        self.check_state()
        ui.update(
            pH=self.pobj.health,
            pC=self.pobj.charge,
            cH=self.eobj.health,
            cC=self.eobj.charge
        )
        self.spcl_ready()