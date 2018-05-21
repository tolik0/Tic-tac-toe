from btree import Tree
from copy import deepcopy


class Board():
    def __init__(self, player="X"):
        self.board = [[" " for i in range(3)] for i in range(3)]
        self.player = player
        self.comput = "O" if player == "X" else "O"

    @staticmethod
    def check_board(board):
        res = [[board[i][i] for i in range(3)]]
        res.append([board[i][2 - i] for i in range(3)])
        res += [[board[i][j] for j in range(3)] for i in range(3)]
        res += [[board[j][i] for j in range(3)] for i in range(3)]

        for s in res:
            if s == ["X" for i in range(3)]:
                return "X"
            elif s == ["O" for i in range(3)]:
                return "O"

        return None if " " in [board[i][j] for i in range(3) for j in \
                               range(3)] else 0

    def __str__(self):
        board = ""
        for i in range(3):
            board += "-------------\n"
            board += "|" + self.board[i][0] + "|" + self.board[i][1] + "|" + \
                     self.board[i][2] + "|\n"
        return board + "-------------"

    def human(self):
        while True:
            coor = input("Input coordinates (Example: 1 2): ")
            try:
                coor = tuple(map(int, coor.split()))
                if 1 <= coor[0] <= 3 and 1 <= coor[1] <= 3:
                    if self.board[coor[0] - 1][coor[1] - 1] == " ":
                        self.board[coor[0] - 1][coor[1] - 1] = self.player
                        break
                    else:
                        print("This cell is not free")
                else:
                    print("Coordinates should be from 1 to 3")
            except:
                print("Wrong input")
                continue

    def computer(self):
        tree = Tree()
        tree.set_root(deepcopy(self.board))

        def new_check(board):
            if self.check_board(board) == self.comput:
                return 1
            elif self.check_board(board) == self.player:
                return -1
            elif self.check_board(board) == 0:
                return 0
            else:
                return None

        def add(item, state=True):
            if self.check_board(item.data) in ["O", 0, "X"]:
                item.res = new_check(item.data)
            else:
                for i in range(3):
                    if len(item.children) == 2:
                        break
                    for j in range(3):
                        if item.data[i][j] == " ":
                            new = deepcopy(item.data)
                            new[i][j] = self.comput if state else self.player
                            tree.add(item, new)
                            add(item.children[-1], state=not state)
                        if len(item.children) == 2:
                            break

        add(tree._root)

        def calculate(item, func):
            if item.res != None:
                return item.res
            item.res = func(item.children, key=lambda x: \
                calculate(x, min if func == max else max)).res
            return item.res

        calculate(tree._root, max)
        board = max(tree._root.children, key=lambda x: x.res)
        self.board = board.data

    def run(self):
        player = "A"
        while player not in "XO":
            player = input("Choose your side (X or O): ")
        self.player = player
        self.comput = "O" if player == "X" else "X"
        print(self)
        state = "hum" if self.player == "X" else "com"
        while self.check_board(self.board) not in ["O", 0, "X"]:
            if state == "com":
                print("Turn of computer")
                self.computer()
                print(self)
                state = "hum"
            else:
                print("Your turn")
                self.human()
                print(self)
                state = "com"
        res = self.check_board(self.board)
        if res == 0:
            print("Draw")
        elif (res == "O" and player == "O") or (res == "X" and player == "X"):
            print("You won!")
        else:
            print("You lost!")


class Clever_Board(Board):
    def computer(self):
        tree = Tree()
        tree.set_root(deepcopy(self.board))

        def new_check(board):
            if self.check_board(board) == self.comput:
                return 1
            elif self.check_board(board) == self.player:
                return -1
            elif self.check_board(board) == 0:
                return 0
            else:
                return None

        def add(item, state=True):
            if self.check_board(item.data) in ["O", 0, "X"]:
                item.res = new_check(item.data)
            else:
                for i in range(3):
                    for j in range(3):
                        if item.data[i][j] == " ":
                            new = deepcopy(item.data)
                            new[i][j] = self.comput if state else self.player
                            tree.add(item, new)
                            add(item.children[-1], state=not state)

        add(tree._root)

        def calculate(item, func):
            if item.res is None:
                item.res = func(item.children, key=lambda x: \
                    calculate(x, min if func == max else max)).res
            return item.res

        calculate(tree._root, max)
        board = max(tree._root.children, key=lambda x: x.res)
        self.board = board.data
