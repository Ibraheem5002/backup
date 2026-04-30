from ursina import *
from game_manager import GM
from module import MarkovChains

# model = MarkovChains()
# if model != None:
#     print(model.predict("A",1))
# else:
#     print("MODULE ERROR")

width = 800
height = 600
bg_height = 450
flr_height = 150

app = Ursina()

window.size = (width,height)
window.borderless = False

camera.orthographic = True
camera.fov = 6

gm = GM()
gm.show_menu()
# gm.show_game()
# gm.show_end()

app.run()