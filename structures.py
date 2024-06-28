"""
Akshay Kumar Mohabey
Python3
Mac OSX
21 June 2024

Rock, Paper, Scissors Game
Structures File
"""
#importing the agent file
import agents
import parameters
import random

players_list = []

for i in range(parameters.num_of_players):
    player = agents.RandomPlayer(i+1)
    players_list.append(player)

for i in range(parameters.num_of_players):
    print(players_list[i])

player = players_list[2]

x = agents.RandomPlayer(32)

print(x.return_ID())


