'''
Level 3-3:
    The idea is that you're given an nxn 'maze' (full of zombies), and a
        bunch of zombie food. You can only travel down and to the right.
    Each 'room' in the maze has a number coresponding to the amount of
        food you have to give that zombie. You must find the path to the
        bottom right (maze position [n,n]) that uses up the most food
        without running out before you get to the end.
    Return how much food you have left. -1 if no solution.
    Ex.
        maze = [1, 0, 3]
               [0, 2, 5]
               [1, 0, 1]
        food = 5
        Answer = 1
        Both the paths
            (0,0) -> (1,0) -> (2,0) -> (2,1) -> (2,2) = [1 + 0 + 1 + 0 + 1] = 3
            and,
            (0,0) -> (1,0) -> (1,1) -> (2,1) -> (2,2) = [1 + 0 + 2 + 0 + 1] = 4
            work. But the second uses up the most food, so it is the path we
            care about. We return 1 because you used up all but one food.

    The solution idea is to start at grid[0][0]. If the value in the first room
        is greater than the amount of food, return -1. Else, the food for that
        box is equal to that box (since there are no rooms above or to the left
        of it.
    You keep going through the rows, collecting all of the possible values of
        the paths leading to it. Usinf the example maze above, all of the
        possible paths leading up to maze[1][1] are
        (0,0) -> (0,1) -> (0,2) = [1 + 2 + 2] = 5
        (0,0) -> (1,0) -> (0,2) = [1 + 0 + 2] = 3
        So the position count_maze[1][1] would contain a list [5,3], where
        count_maze is a new maze that holds all of the values of each path.
    To avoid needlessly re-checking values that don't work, we only append them
        if they are less than or equal to the amount of food given.
    So if you were making a list for maze[2][2], you'd have list
        maze[1][2] = [5,3]
        maze[2][0] = [4] (its the top-most column, so it only has from left)
        You therefore have [3,4,5] that could all be added to the 5 currently
        in that room.
        3 + 5 = 8
        4 + 5 = 9
        5 + 5 = 10
    Because all of these new values are greater that the amount of food you
        were given, an empty list is placed in that count_maze position.
    When you get to the final room, you just find the largest value from the
        surrounding rooms that is still less than or equal to the food you
        have when added to the value in the final box.
'''
# Four test cases used
food1 = 7
grid1 = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
food2 = 12
grid2 = [[0, 2, 5], [1, 1, 3], [2, 1, 1]]
food3 = 20
grid3 = [[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],
         [0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]]
# Sorry/Not sorry for the ugly 10x10
food4 = 50
grid4 = [[0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9],
         [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9],
         [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9],
         [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9],
         [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9],
         [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9],
         [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9],
         [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9],
         [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9],
         [0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9]]
def zombIt(food, grid):
    n = len(grid)
    new = []
    for x in range(n):
        row = []
        for y in range(n):
            z = grid[x][y]
            if (x == 0) and (y == 0):
                if (z <= food):
                    box = [z]
                else:
                    return -1
            elif (x == 0):
                if (z <= food):
                    box = [z + grid[0][y-1]]
            elif (y == 0):
                if (z <= food):
                    box = [z + grid[x-1][0]]
            else:
                box = []
                for e in new[x-1][y]:
                    if (z+e) <= food:
                        box.append(z+e)
                for e in row[y-1]:
                    if ((e+z) not in box) and ((e+z) <= food):
                        box.append(e+z)
            row.append(box)
        new.append(row)
    largest = -1
    for x in new[n-1][n-1]:
        if (largest < x <= food):
            largest = x
    if largest != -1:
        largest = (food - largest)
    return largest

print zombIt(food1, grid1) # 0
print zombIt(food2, grid2) # 1
print zombIt(food3, grid3) # -1
print zombIt(food4, grid4) # -1
# Passes all test cases
