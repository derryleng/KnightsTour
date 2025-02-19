import csv
from datetime import datetime
import random

total_attempts = 50000 # Set number of games to play
board_size = 8 # Set size of board
start_position = [0,0] # Set start position
tour_type = "warnsdorf" # Choose type of tour to take

def valid_moves(position):
    x = [[position[0]-1,position[1]-2],
        [position[0]+1,position[1]-2],
        [position[0]+2,position[1]-1],
        [position[0]+2,position[1]+1],
        [position[0]+1,position[1]+2],
        [position[0]-1,position[1]+2],
        [position[0]-2,position[1]+1],
        [position[0]-2,position[1]-1]]
    i = 0
    while i < len(x):
        if x[i][0] < 0 or x[i][0] >= board_size or x[i][1] < 0 or x[i][1] >= board_size or x[i] in move_history:
            x.pop(i)
        else:
            i += 1
    return(x)

def random_tour(position):
    while len(valid_moves(position)) > 0:
        move_history.append(position)
        position = random.choice(valid_moves(position))

def frodsnraw_tour(position):
    while len(valid_moves(position)) > 0:
        move_history.append(position)
        moves_rank = [len(valid_moves(x)) for x in valid_moves(position)]
        moves_choice = random.choice([i for i, j in enumerate(moves_rank) if j == max(moves_rank)])
        position = valid_moves(position)[moves_choice]

def warnsdorf_tour(position):
    while len(valid_moves(position)) > 0:
        move_history.append(position)
        moves_rank = [len(valid_moves(x)) for x in valid_moves(position)]
        moves_choice = random.choice([i for i, j in enumerate(moves_rank) if j == min(moves_rank)])
        position = valid_moves(position)[moves_choice]

headers = [["Attempt", "Num_Moves", "Progress", "Moves"]]
timestamp = "".join(str(x) for x in str(datetime.now().strftime("%Y%m%d%H%M%S")))
filename = "tour_{}_size{}_{}.csv".format(timestamp, board_size, tour_type)
with open(filename, "w") as file:
    writer = csv.writer(file)
    writer.writerows(headers)
    for i in range(0,total_attempts):
        position = start_position 
        move_history = []
        if tour_type == "random":
            random_tour(position)
        elif tour_type == "frodsnraw":
            frodsnraw_tour(position)
        elif tour_type == "warnsdorf":
            warnsdorf_tour(position)
        row = [[i+1, len(move_history), "{}%".format(len(move_history)/(board_size**2)*100), move_history]]
        writer.writerows(row)
    file.close()
