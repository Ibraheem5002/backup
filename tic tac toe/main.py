from game import Game
from player import Player
from model import Model
import menu
import msvcrt

def main():

    while True:
        choice = menu.menu()
        game = Game()

        if choice == 0: pvp(game)
        elif choice == 1: pvc(game)
        elif choice == 2: cvc(game)
        else: return

        print("\nPress any button to continue")
        msvcrt.getch()

def pvp(game: Game):
    p1 = Player("O", "P1")
    p2 = Player("X", "P2")

    while True:
        game.print_grid()
        game.create_empty_space()

        if game.p1_turn:
            move = p1.take_input(game.grid)
            game.in_p1.append(move)
            game.apply_move(move, p1.symbol)
        else:
            move = p2.take_input(game.grid)
            game.in_p2.append(move)
            game.apply_move(move, p2.symbol)

        if game.check_win():
            game.print_grid()
            if game.p1_turn:
                print("P1 WINS !!!")
            else:
                print("P2 WINS !!!")
            break

        game.p1_turn = not game.p1_turn

def pvc(game:Game):
    p1 = Player("O","P1")
    p2 = Model("X","O")

    while True:
        game.print_grid()
        game.create_empty_space()

        if game.p1_turn:
            move = p1.take_input(game.grid)
            game.in_p1.append(move)
            game.apply_move(move, p1.symbol)
        else:
            move = p2.predict(game.grid,game.in_p2)
            game.in_p2.append(move)
            game.apply_move(move,p2.m1)

        if game.check_win():
            game.print_grid()
            if game.p1_turn:
                print("P1 WINS !!!")
            else:
                print("P2 WINS !!!")
            break

        game.p1_turn = not game.p1_turn

def cvc(game:Game):
    p1 = Model("O","X")
    p2 = Model("X","O")

    while True:
        game.print_grid()
        game.create_empty_space()

        if game.p1_turn:
            move = p1.predict(game.grid,game.in_p1)
            game.in_p1.append(move)
            game.apply_move(move, p1.m1)
        else:
            move = p2.predict(game.grid,game.in_p2)
            game.in_p2.append(move)
            game.apply_move(move,p2.m1)

        if game.check_win():
            game.print_grid()
            if game.p1_turn:
                print("P1 WINS !!!")
            else:
                print("P2 WINS !!!")
            break

        game.p1_turn = not game.p1_turn


main()