import os
import shutil
import msvcrt

def menu():
    options = ["Player vs Player", "Player vs CPU", "CPU vs CPU","Exit"]
    choice = 0 

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        columns = shutil.get_terminal_size().columns
        
        print("\n" * 2)
        print("Tic Tac Toe".center(columns))
        print(("-" * 11).center(columns))
        print("\n")

        for i in range(len(options)):
            if i == choice:
                text = f"→ {options[i]}"
            else:
                text = f"  {options[i]}"
            print(text.center(columns))

        key = msvcrt.getch()

        if key in [b'\xe0', b'\x00']:
            sub_key = msvcrt.getch()
            if sub_key == b'H':   # up
                choice = (choice - 1) % len(options)
            elif sub_key == b'P': # down
                choice = (choice + 1) % len(options)
        
        elif key == b'\r': # enter
            return choice
