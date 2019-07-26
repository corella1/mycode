#!/usr/bin/env python3

from random import randint

class Player:
    def _init_(self, first_name):
        self.dice = []
        self.name = first_name

    def roll(self):
        self.dice = []
        for i in range(3):
            self.dice.append(randint(1,6))

    def get_dice(self):
        return self.dice

    def name(self):
        return self.name

player1 = Player()
player2 = Player()

player1.roll()

print(f'Player {player1.name}  rolled {player1.get_dice()}')


