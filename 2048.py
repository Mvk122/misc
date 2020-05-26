import random 
from copy import deepcopy

def move(array, move):
    if move not in ['up', 'down', 'left', 'right']:
        print("invalid move")
        return array
        
    #does the move and adds a 2 or a 4 to the array
    if move == "up":
        #first the second layer is considered
        for index in range(3):
            if array[1][index] == array[0][index]:
                array[0][index] += array[1][index]
                array[1][index] = 0 
            elif array[0][index] == 0:
                array[0][index] += array[1][index]
                array[1][index] = 0
        #then the relationship between the second and third layer is considered 
        for index in range(3):
            if array[1][index] == 0:
                if array[0][index] == array[2][index]:
                    array[0][index] += array[2][index]  
                    array[2][index] = 0
                if array[0][index] == 0:
                    array[0][index] += array[2][index]
                    array[2][index] = 0
                array[1][index] += array[2][index]
                array[2][index] = 0  
            elif array[1][index] == array[2][index]:
                array[1][index] += array[2][index]
                array[2][index] = 0         
    
    if move == "down":
        #first the third layer is considered 
        for index in range(3):
            if array[1][index] == array[2][index]:
                array[2][index] += array[1][index]
                array[1][index] = 0 
            elif array[2][index] == 0:
                array[2][index] += array[1][index]
                array[1][index] = 0       
        #then the second and first is considered
        for index in range(3):
            if array[1][index] == 0:
                if array[2][index] == array[0][index]:
                    array[2][index] += array[0][index]  
                    array[0][index] = 0
                if array[2][index] == 0:
                    array[2][index] += array[0][index]
                    array[0][index] = 0
                array[1][index] += array[0][index]
                array[0][index] = 0  
            elif array[2][index] == array[1][index]:
                array[2][index] += array[1][index]
                array[1][index] = 0
            elif array[1][index] == array[0][index]:
                array[1][index] += array[0][index]
                array[0][index] = 0 


    if move == "left":
        for layer in array:
            #cosider the left most and the second left first
            if layer[0] == layer[1]:
                layer[0] += layer[1]
                layer[1] = 0 
            elif layer[0] == 0:
                layer[0] += layer[1]
                layer[1] = 0  
            #then consider the second and third from the left
        for layer in array:
            if layer[1] == 0:
                if layer[0] == 0:
                    layer[0] += layer[2]
                    layer[2] = 0
                if layer[0] == layer[2]:
                    layer[0] += layer[2]
                    layer[2] = 0
                layer[1] += layer[2]
                layer[2] = 0   
            elif layer[1] == layer[2]:
                layer[1] += layer[2]
                layer[2] = 0 


    if move == "right":
        #consider the right most and the second right first 
        for layer in array:
            if layer[2] == layer[1]:
                layer[2] += layer[1]
                layer[1] = 0 
            elif layer[2] == 0:
                layer[2] += layer[1]
                layer[1] = 0
        #consider the second and third from the right
        for layer in array:
            if layer[1] == 0:
                if layer[2] == 0:
                    layer[2] += layer[0]
                    layer[0] = 0
                if layer[2] == layer[0]:
                    layer[2] += layer[0]
                    layer[0] = 0
                layer[1] += layer[0]
                layer[0] = 0   
            elif layer[1] == layer[0]:
                layer[1] += layer[0]
                layer[0] = 0
 
    found = False 
    while not found:
        i = 0 
        for line in array:
            if 0 not in line:
                i += 1
        if i == 3:
            break 
        choicelist = [4,2,2,2,2]
        number = random.choice(choicelist)
        randx = random.randint(0,2)
        randy = random.randint(0,2)
        if array[randy][randx] == 0:
            found = True 
            array[randy][randx] = number

    return array

def checkstate(array):
    counter = 0
    secondarray = deepcopy(array)

    for mover in ['up', 'down', 'left', 'right']:
        if move(secondarray, mover) == array:
            counter += 1 
    if counter == 4:
        return False 
    else:
        return True 


def getscore(array):
    counter = 0 
    for layer in array:
        for element in layer:
            counter += element
    return counter

gamearray = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
#TODO: fix how numbers dont join downwards from up and second top layer 
for array in gamearray:
    print(array)
#AutoPlayer
def autoplay(gamearray):
    while True:
        direction = random.choice(['up', 'down', 'left', 'right'])
        newarray = move(gamearray, direction)
        print("Your Move:   ", direction)
        for array in newarray:
            print(array)
        if not checkstate(newarray):
            print("GAME OVER")
            print("your Final score is:  ", getscore(newarray))
            break
        print(' ')
    gamearray = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    return getscore(newarray)


#PlayerCountrolled
def playerrun(gamearray): 
    while True:
        playermove = input("Which direction to move?:     ")
        newarray = move(gamearray, playermove)
        for array in newarray:
            print(array)
        if not checkstate(newarray):
            print('GAME OVER')
            print(getscore(newarray))
            break 
        print(' ')
    return getscore(newarray)

"""
highestscore = 0 
for i in range(1000):
    score = autoplay(gamearray)
    gamearray = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    if score > highestscore:
        highestscore = score
print('highest:   ', highestscore)
"""
playerrun(gamearray)
input('PRESS ENTER TO EXIT')
