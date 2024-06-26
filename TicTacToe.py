from random import randint

def print_grid(grid):
    print("_ _ _ _ _ _ __")
    print(f"| {grid[0]} | {grid[1]} | {grid[2]} |")
    print("_ _ _ _ _ _ _ ")
    print(f"| {grid[3]} | {grid[4]} | {grid[5]} |")
    print("_ _ _ _ _ _ _ ")
    print(f"| {grid[6]} | {grid[7]} | {grid[8]} |")
    print("_ _ _ _ _ _ _ ")

def choose_marker():
    while True:
        player1 = input("Player 1, choose 'X' or 'O': ").upper()
        if player1 in ['X', 'O']:
            player2 = 'O' if player1 == 'X' else 'X'
            print(f"\nPlayer 1 is {player1}")
            print(f"Player 2 is {player2}")
            return player1, player2
        else:
            print("Invalid choice. Please choose 'X' or 'O'.")

def choose_first(player1, player2):
    return player1 if randint(0, 1) == 0 else player2

def is_draw(grid):
    return " " not in grid

def is_winner(grid, player):
    win_conditions = [
        [grid[0], grid[1], grid[2]],
        [grid[3], grid[4], grid[5]],
        [grid[6], grid[7], grid[8]],
        [grid[0], grid[3], grid[6]],
        [grid[1], grid[4], grid[7]],
        [grid[2], grid[5], grid[8]],
        [grid[0], grid[4], grid[8]],
        [grid[2], grid[4], grid[6]],
    ]
    return [player, player, player] in win_conditions

def make_choice(grid, choice, player):
    grid[choice - 1] = player
    print_grid(grid)
    print("Successfully inserted")

def replay():
    while True:
        choose = input("The game is finished. Do you want to continue playing (Y or N)? ").upper()
        if choose == 'Y':
            return True
        elif choose == 'N':
            return False
        else:
            print("Invalid choice. Please enter 'Y' or 'N'.")

def play_game():
    print("Welcome to tic tac toe game!")

    while True:
        grid = [" " for _ in range(9)]
        player1, player2 = choose_marker()
        turn = choose_first(player1, player2)
        print(f"{turn} will go first.")
        
        game_on = True
        
        while game_on:
            print(f"{turn}'s turn")
            
            while True:
                try:
                    choice = int(input("Please choose a position (1-9): "))
                    if choice in range(1, 10) and grid[choice - 1] == " ":
                        break
                    else:
                        print("Invalid move. The position is either occupied or out of range.")
                except ValueError:
                    print("Please enter a number between 1 and 9.")

            make_choice(grid, choice, turn)

            if is_winner(grid, turn):
                print(f"The game is won by {turn}")
                game_on = False
            elif is_draw(grid):
                print("The game is a draw")
                game_on = False
            else:
                turn = player1 if turn == player2 else player2

        if not replay():
            print("Thanks for playing!")
            break

play_game()
