from board import Board, Clever_Board

choice = input("Do you want to play a tic-tac-toe (y or n): ")
while choice == "y":
    mode = input("Choose mode (clever or stupid): ")
    if mode == "clever":
        print("Mode is clever")
        game = Clever_Board()
        game.run()
    else:
        print("Mode is stupid")
        game = Board()
        game.run()
    choice = input("Do you want to play a tic-tac-toe (y or n): ")
