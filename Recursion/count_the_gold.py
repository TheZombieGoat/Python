"""
File : count_the_gold.py
Date : 04/21/2023
"""

PASSABLE = "_"
GOLD = "G"
BLOCKED = "*"
VISITED = 'V'

import random

def sum_gold(gold_list):
        gold = 0
        for i in gold_list:
                gold = gold + i
        return gold

def create_map(seed, rows, cols):
    random.seed(seed)
    the_map = [[random.choices([PASSABLE, BLOCKED, GOLD], weights=[5, 2, 1])[0] for _ in range(cols)] for _ in range(rows)]
    the_map[0][0] = PASSABLE
    for i in range(rows):
        for j in range(cols):
            if the_map[i][j] == GOLD:
                the_map[i][j] = GOLD + str(random.randint(1, 9))
    return the_map


def display_map(the_map):
    for row in the_map:
        for x in row:
            print(x.rjust(3), end='')
        print()


def count_the_gold(treasure_map, current_pos,height,width,gold_list):
        current_x = current_pos[1]
        current_y = current_pos[0]

        if treasure_map[current_y][current_x] == VISITED:
                return
 #collecting gold and appending it to a list to return later.
        if GOLD in treasure_map[current_y][current_x]:
                gold_list.append(int(treasure_map[current_y][current_x][1:]))
                treasure_map[current_y][current_x] = VISITED

        if PASSABLE in treasure_map[current_y][current_x]:
                treasure_map[current_y][current_x] = VISITED

        #go right
        if current_x + 1 < width and treasure_map[current_y][current_x+1] != BLOCKED:
                count_the_gold(treasure_map,(current_y,current_x+1),height,width,gold_list)
        #go left
        if current_x - 1 >= 0 and treasure_map[current_y][current_x-1] != BLOCKED:
                count_the_gold(treasure_map,(current_y,current_x-1),height,width,gold_list)
        #go down
        if current_y + 1 < height and treasure_map[current_y+1][current_x] != BLOCKED:
                count_the_gold(treasure_map,(current_y+1,current_x),height,width,gold_list)
        #go up
        if current_y - 1 >= 0 and treasure_map[current_y-1][current_x] != BLOCKED:
                count_the_gold(treasure_map,(current_y-1,current_x),height,width,gold_list)

        # return sum_gold(gold_list)


if __name__ == '__main__':
    my_map = create_map(*list(map(int, input('Enter seed rows cols separated by spaces: ').split())))
    display_map(my_map)
    print('Counting the gold...')
    height = len(my_map)
    width = len(my_map[0])
    gold_list = []
    count_the_gold(my_map, [0, 0],height,width,gold_list)
    value = sum_gold(gold_list)
    display_map(my_map)
    print('The total value of gold we can reach is: ', value)
