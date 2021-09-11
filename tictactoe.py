import random


class Board:  # Board object
    def __init__(self):
        # Represent empty spaces on the board
        self.column1 = [" ", " ", " "]
        self.column2 = [" ", " ", " "]
        self.column3 = [" ", " ", " "]

    def update(self):
        # Draws the board
        print(f"\n{self.column1[0]} | {self.column1[1]} | {self.column1[2]}\n"
              f"{self.column2[0]} | {self.column2[1]} | {self.column2[2]}\n"
              f"{self.column3[0]} | {self.column3[1]} | {self.column3[2]}\n")

    def clear(self):
        # Resets the board
        self.column1 = [" ", " ", " "]
        self.column2 = [" ", " ", " "]
        self.column3 = [" ", " ", " "]


class Player:  # Player object
    def __init__(self):
        self.score = 0
        self.pick = None  # Location of player's move
        self.pref = None  # X or O
        self.win = None  # Tells whether the Player object has won

    def attempt(self):  # Draws player's move on board
        if self.pick == 1:
            board.column3[0] = self.pref
        if self.pick == 2:
            board.column3[1] = self.pref
        if self.pick == 3:
            board.column3[2] = self.pref
        if self.pick == 4:
            board.column2[0] = self.pref
        if self.pick == 5:
            board.column2[1] = self.pref
        if self.pick == 6:
            board.column2[2] = self.pref
        if self.pick == 7:
            board.column1[0] = self.pref
        if self.pick == 8:
            board.column1[1] = self.pref
        if self.pick == 9:
            board.column1[2] = self.pref

        # Below are win conditions
        # if a horizontal line is formed:
        if (self.pref == board.column1[0] == board.column1[1] == board.column1[2]) or (
                    self.pref == board.column2[0] == board.column2[1] == board.column2[2]) or (
                    self.pref == board.column3[0] == board.column3[1] == board.column3[2]):
            self.win = True

        # if a diagonal line is formed:
        if (self.pref == board.column1[0] == board.column2[1] == board.column3[2]) or (
                    player.pref == board.column3[0] == board.column2[1] == board.column1[2]):
            self.win = True

        # if a vertical line is formed:
        if (self.pref == board.column1[0] == board.column2[0] == board.column3[0]) or (
                    player.pref == board.column1[1] == board.column2[1] == board.column3[1]) or (
                    player.pref == board.column1[2] == board.column2[2] == board.column3[2]):
            self.win = True

# Instantiate Player and Board instances


player = Player()
computer = Player()
board = Board()


class Game:  # Game object
    def __init__(self):
        self.items = ["X", "O"]  # Characters the player can use
        self.running = True  # Set to False to exit the game
        player.win = False
        computer.win = False
        self.choices = [x for x in range(1, 10)]  # List of available spaces on the board

    def run(self):  # Main game loop

        def reset():  # Resets the number of spaces of available spaces on the board
            for x in range(1, 10):
                self.choices.append(x)  # Adds spaces back to the board
            player.win = False  # Resets win indicators for both player and computer
            computer.win = False
                
        if not self.running:
            exit()  # Game will exit when self.running is set to False
        else:
            def ask_pref():  # Asks the user which character to use (X or O)
                player.pref = input("What do you prefer to use? (X/O)").upper()  # Makes user input all caps to match characters in self.items

                if player.pref not in self.items:  # For inputs not in self.items
                    print("Invalid input!")
                    ask_pref()

                if player.pref == self.items[0]:  # If user input is X
                    computer.pref = self.items[1]
                    print(f"You picked {player.pref}!")
                    board.update()

                else:
                    print(f"You picked {player.pref}")  # If user input is O
                    computer.pref = self.items[0]
                    board.update()


            def close():  # Asks the user to play again or to exit the game
                cont_list = ["Y", "N"]
                cont_game = input("Would you like to play again? (Y/N)").upper()
                if cont_game not in cont_list:
                    print("Invalid input!")
                    close()

                elif cont_game == cont_list[0]:
                    board.clear()
                    reset()
                    self.run()

                elif cont_game == cont_list[1]:
                    print("Thank you for playing!")
                    self.running = False
                    self.run()

            def play():  # Recurring game loop representing the player turn
                # Reset board if no empty spaces are available on the board and no one has won yet
                if len(self.choices) == 0 and not player.win and not computer.win:
                    print("No more moves left! Let's play again!")
                    board.clear()
                    play()

                if player.win:
                    print("You win!")
                    close()

                if computer.win:
                    print("You lose!")
                    close()

                else:
                    player.pick = int(input("Place your pick!"))  # Asks the user to make a move on the board
                    if player.pick not in self.choices:  # Indicates that the space on the board chosen by user is not empty
                        print("Place already taken! Try again!")
                        play()
                    else:  # If chosen space on the board is still available
                        player.attempt()  # Draws the player's move on the board
                        self.choices.remove(player.pick)  # Removes space from list of empty spaces; indicates space is taken to avoid repetition of moves

                        computer.pick = random.choice(self.choices)  # Draws the computer's move on the board
                        computer.attempt()  # Draws the computer's move on the board
                        self.choices.remove(computer.pick)  # Removes space from list empty spaces
                        board.update()  # Updates the board

                        play()

            print("Tictac Toe game\nUse the numpad to place your pick")
            ask_pref()
            play()


game = Game()

if __name__ == "__main__":
    game.run()
