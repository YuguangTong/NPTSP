from random import randint
import numpy as np
import sys

if len(sys.argv) != 3:
    print("usage: python3 in_gen.py [n] [filename]")
    sys.exit(0)
elif int(sys.argv[1])%2 == 1:
    print("%d should be a constant", n)
    sys.exit(0)
else:
    n = int(sys.argv[1])
    filename = sys.argv[2]
    myFile = open(filename, 'w')
    arr = np.zeros((n, n), int)
    redCounter = 0
    blueCounter = 0
    color = ''
    for i in range(n):
        for j in range(i):
            arr[i, j] = randint(0, 100)
            arr[j, i] = arr[i, j]
        if (randint(0, 1) == 0 and redCounter < n/2) \
                or blueCounter == n/2:
            color +='R'
            redCounter += 1
        else:
            color += 'B'
            blueCounter += 1

    myFile.write(str(n) + '\n')
    for i in range(n):
        line = ''
        for j in range(n):
            line += str(arr[i, j]) + ' '
        myFile.write(line + '\n')
    myFile.write(color + '\n')
    myFile.close()

