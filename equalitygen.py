from random import randint
import sys

if len(sys.argv) != 3:
    print("usage: python3 in_gen.py [number of cities] [filename]")
    sys.exit(0)
elif int(sys.argv[1])%2 == 1:
    print("The first argument should be a constant divisible by 2")
    sys.exit(0)
else:
    num_cities = int(sys.argv[1])
    filename = sys.argv[2]
    myFile = open(filename, 'w')
    arr = [[0 for _ in range(num_cities)] for _ in range(num_cities)]
    redCounter = 0
    blueCounter = 0
    color = ''
    for i in range(num_cities):
        if (randint(0, 1) == 0 and redCounter < num_cities/2) \
                or blueCounter == num_cities/2:
            color +='R'
            redCounter += 1
        else:
            color += 'B'
            blueCounter += 1
    for i in range(num_cities):
        for j in range(i):
            if color[i] == color[j]:
                arr[i][j] = randint(0, 10)
            else:
                arr[i][j] = randint(90, 100)
            arr[j][i] = arr[i][j]

    myFile.write(str(num_cities) + '\n')
    for i in range(num_cities):
        line = ''
        for j in range(num_cities):
            line += str(arr[i][j]) + ' '
        myFile.write(line + '\n')
    myFile.write(color + '\n')
    myFile.close()

