class Player:
    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name

    def take_input(self, grid):
        print(f"{self.name} ({self.symbol}) Turn")
        print("input x and y respectively:")

        while True:
            y = input()
            x = input()

            if x not in ['0','1','2'] or y not in ['0','1','2']:
                print("input again")
                continue

            x = int(x)
            y = int(y)

            if grid[x][y] == " ":
                return [x, y]

            print("input again")