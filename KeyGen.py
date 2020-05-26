import string
import random
import time 

validcharacters = string.ascii_letters + '1234567890'

def generatekey(blocksize, blockcount, validcharacters):
    key = ''
    for _ in range(blockcount -1 ): 
        key += randomblock(blocksize, validcharacters)
        key += "-"
    key += randomblock(blocksize, validcharacters)
    return key

def keycracker(validkeys, blocksize, blockcount, validcharacters):
    key = ''
    guesses = 0 
    start = time.time()
    while key not in validkeys:
        key = generatekey(blocksize, blockcount, validcharacters)
        guesses += 1 
    end = time.time()
    print( "%s is a valid key, %s guesses were tried, cracking took %s seconds" %(key ,str(guesses), str(end - start)))


def randomblock(size, validcharacters):
    output = ''
    for _ in range(size):
        output += random.choice(validcharacters)
    return output


if __name__ == "__main__":
    while True:
        print(str(generatekey(5,4,validcharacters))) 