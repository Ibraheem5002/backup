import random
import time
from collections import defaultdict

class Model:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
        self.out_x = 3
        self.out_y = 3

    def predict(self,grid:list,in_p1:list,in_p2:list):
        time.sleep(0.5)

        self.grid = grid
        self.in_p1 = in_p1
        self.in_p2 = in_p2

        if self.imm_win(): return (self.out_x,self.out_y)
        if self.imm_block(): return (self.out_x,self.out_y)

        # min max
        self.options = {}   # coordinates : points
        for x,y in self.get_free_spaces(self.grid):
            self.options[(x,y)] = self.minmax(self.grid,True,(x,y))
        
        for i in [1,0,-1]:
            op = [keys for keys, values in self.options.items() if i == values]
            if op:
                return random.choice(op)
    
    def get_free_spaces(self,grid1:list):
        spaces = []
        for i in range(3):
            for j in range(3):
                if grid1[i][j] == " ": spaces.append((i,j))
        return spaces
        
    def check_win(self,grid1:list):
        for i in range(3):
            if grid1[i][0] == grid1[i][1] == grid1[i][2] == self.m1: return True
            if grid1[0][i] == grid1[1][i] == grid1[2][i] == self.m1: return True
        
        if grid1[0][0] == grid1[1][1] == grid1[2][2] == self.m1: return True
        if grid1[2][0] == grid1[1][1] == grid1[0][2] == self.m1: return True
        return False
    
    def check_lose(self,grid1:list):
        for i in range(3):
            if grid1[i][0] == grid1[i][1] == grid1[i][2] == self.m2: return True
            if grid1[0][i] == grid1[1][i] == grid1[2][i] == self.m2: return True
        
        if grid1[0][0] == grid1[1][1] == grid1[2][2] == self.m2: return True
        if grid1[2][0] == grid1[1][1] == grid1[0][2] == self.m2: return True
        return False
        
    def check_draw(self,grid1:list):
        if self.get_free_spaces(grid1) != []:
            return False
        return True
    
    def minmax(self,grid1:list,my_turn:bool,space=list):
        x,y = space
        grid2 = [row[:] for row in grid1]

        if my_turn: grid2[x][y] = self.m1
        else: grid2[x][y] = self.m2

        if self.check_win(grid2): return 1
        elif self.check_lose(grid2): return -1
        elif self.check_draw(grid2): return 0

        scores = []
        for sp in self.get_free_spaces(grid2):
            scores.append(self.minmax(grid2,not my_turn,sp))
        
        return max(scores) if my_turn else min(scores)
    
    def imm_win(self,grid1:list):
        if len(self.in_p1) >= 3:
            x,y = self.in_p1[0]
            grid1[x][y] = " "

        for r_idx,row in enumerate(grid1):
            if row.count(self.m1) == 2 and " " in row:
                self.out_x = r_idx
                self.out_y = row.index(" ")
                return True
        
        for c_idx,col in enumerate(zip(*grid1)):
            if col.count(self.m1) == 2 and " " in col:
                self.out_x = col.index(" ")
                self.out_y = c_idx
                return True
        
        diag = [(0,0),(1,1),(2,2)]
        vals = [grid1[x][y] for x,y in diag]
        if vals.count(self.m1) == 2 and " " in vals:
            idx = vals.index(" ")
            self.out_x, self.out_y = diag[idx]
            return True

        diag = [(0,2),(1,1),(2,0)]
        vals = [grid1[x][y] for x,y in diag]
        if vals.count(self.m1) == 2 and " " in vals:
            idx = vals.index(" ")
            self.out_x, self.out_y = diag[idx]
            return True
        return False
    
    def imm_block(self,grid1:list):
        if len(self.in_p2) >= 3:
            x,y = self.in_p2[0]
            grid1[x][y] = " "

        for r_idx,row in enumerate(grid1):
            if row.count(self.m2) == 2 and " " in row:
                self.out_x = r_idx
                self.out_y = row.index(" ")
                return True
            
        for c_idx,col in enumerate(zip(*grid1)):
            if col.count(self.m2) == 2 and " " in col:
                self.out_x = col.index(" ")
                self.out_y = c_idx
                return True
        
        diag = [(0,0),(1,1),(2,2)]
        if diag.count(self.m2) == 2 and " " in diag:
            self.out_x = diag.index(" ")
            self.out_y = diag.index(" ")
            return True
        
        diag = [(0,2),(1,1),(2,0)]
        if diag.count(self.m2) == 2 and " " in diag:
            self.out_x = diag.index(" ")
            self.out_y = diag.index(" ")
            return True
        return False