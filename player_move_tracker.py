from abc import ABC, abstractmethod
import random

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]

    def make_move(self):
        move = random.choice(self.moves)
        self.position = (self.position[0] + move[0], self.position[1] + move[1])
        self.path.append(self.position)
        return self.position

    @abstractmethod
    def level_up(self):
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves = [(1,0), (0,1), (-1, 0), (0, -1)]

    def level_up(self):
        extra_moves = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for i in extra_moves:
            self.moves.append(i)
        return self.moves 

player = Pawn()
#print(player.moves)
#print(player.position)
player.make_move()
#print(player.position)
#print(player.path)
player.level_up()
print(player.moves)
player.make_move()
print(player.path)