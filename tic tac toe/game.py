import os

class Game:
    def __init__(self):
        self.grid = [
            [" "," "," "],
            [" "," "," "],
            [" "," "," "]
        ]

        self.in_p1 = []
        self.in_p2 = []

        self.p1_turn = True

    def print_grid(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        print("    0   1   2")
        for i, row in enumerate(self.grid):
            print(f"{i} | " + " | ".join(row) + " |")
            print("  " + "-" * 13)

    def apply_move(self, move, player_symbol):
        x, y = move
        self.grid[x][y] = player_symbol

    def create_empty_space(self):
        if len(self.in_p1) >= 3:
            x,y = self.in_p1[0]
            self.in_p1.pop(0)
            self.grid[x][y] = " "
        
        if len(self.in_p2) >= 3:
            x,y = self.in_p2[0]
            self.in_p2.pop(0)
            self.grid[x][y] = " "

    def check_win(self):
        for x in range(3):
            if self.grid[x][0] == self.grid[x][1] == self.grid[x][2] and self.grid[x][0] != " ": return True
        
        for y in range(3):
            if self.grid[0][y] == self.grid[1][y] == self.grid[2][y] and self.grid[0][y] != " ": return True
        
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] and self.grid[1][1] != " ": return True
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] and self.grid[1][1] != " ": return True

        return False