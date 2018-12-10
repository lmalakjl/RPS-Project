import random

moves = ["rock", "paper", "scissors"]


class Player:

    def move(self):
        return "rock"

    def learn(self, p1, p2):

        pass


class RandomPlayer(Player):

    def move(self):
        choice = random.choice(moves)
        return choice


class CyclePlayer(Player):

    index = 0

    def __init__(self):
        Player.__init__(self)
        self.last_p1 = None

    def move(self):
        self.index += 1
        return moves[self.index % 3]

    def play(self):
        move = None
        if self.last_p1 is None:
            move = Player.play(self)
        else:
            choice = moves.choice(self.last_p1) + 1
            if choice >= len(moves):
                choice = 0
            p1 = moves[choice]
        self.last_p1 = move
        return move


class HumanPlayer(Player):

    def move(self):
        choice = input("What's your play (rock, paper, or scissors)? ")
        while choice not in moves:
            choice = input("Try Again: What's your play? ")
        return choice


class RepeatPlayer(Player):

    def move(self):
        return "rock"


class ReflectPlayer(Player):

    def __init__(self):
        Player.__init__(self)
        self.last_p2 = None

    def move(self):
        if self.last_p2 is None:
            self.last_p2 = random.choice(moves)
        else:
            choice = self.last_p2
        return self.last_p2

    def learn(self, last_p2):
        self.last_p2 = last_p2


def beats(one, two):

    return(
        (one == "rock" and two == "scissors") or
        (one == "scissors" and two == "paper") or

        (one == "paper" and two == "rock")
        )


class Game:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1.score = 0
        self.p2.score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if move1 == move2:
            print("TIE")
        elif beats(move1, move2):
            self.p1.score += 1
            print("Player 1 is Win :) ")
            print("Score is: ", + self.p1.score)
        else:
            self.p2.score += 1
            print("Player 2 is Win :( ")
            print("Score is: ", + self.p2.score)

    def play_game(self):
        print("Game Start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
            print("Game over!")


if __name__ == "__main__":
    choice = input("Hi!\nPlz,Select which player do u want to play with it:")
    while True:
        if choice == "z":
            print("Goodbye!\nIt was nice seeing you :) ")
            exit()
        elif choice == "random":
            game = Game(HumanPlayer(), RandomPlayer())
            game.play_game()
            break
        elif choice == "repeat":
            game = Game(HumanPlayer(), RepeatPlayer())
            game.play_game()
            break
        elif choice == "reflect":
            game = Game(HumanPlayer(), ReflectPlayer())
            game.play_game()
            break
        elif choice == "cycle":
            game = Game(HumanPlayer(), CyclePlayer())
            game.play_game()
            break
        else:
            print("")
            choice = input("Isn't a valid move,Try again!")
