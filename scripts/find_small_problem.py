import os

# script to find out instances with size 20 or smaller

os.chdir(os.path.expanduser('instances/'))
small_count  = 0
for t in range(1, 496):
    fin = open(str(t) + ".in", "r")
    N = int(fin.readline())
    if N <= 20:
        print "instance #: ", t, "\t city #:", N
        small_count += 1
    fin.close()
print "# instance whose size <=20: ", small_count
    

