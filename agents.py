"""
Akshay Kumar Mohabey
Python3
Mac OSX
21 June 2024

Rock, Paper, Scissors Game
Agents File
"""

import random 

import parameters as p

class RandomPlayer(object):
    def __init__(self,ID):
        self.ID = ID
        self.move_history = []
        self.result_hisory = []
        # self.name = name
    
    def __str__(self):
        return str(self.ID)
    
    def return_ID(self):
        return self.ID

    def move(self):
        return random.choices(p.options)
    
    def record_move_history(self,move):
        self.move_history.append(move)
    
    def record_result_history(self, result):
        self.result_history.append(result)

    def print_move_history(self):
        print(self.move_history)

