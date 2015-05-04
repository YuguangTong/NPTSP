import sys
import os

# assumes output file is well formatted
# if you have errors, make sure you double check the output format 
  
def main(argv):
  fanswer = open("answer.out", "r")
  fout = open("score.txt", "w")
  for i in xrange(ninstances):
    finstance = open(os.path.expanduser(input_dir) + `i+1`+".in", "r")
    N = int(finstance.readline())
    d = [[] for i in range(N)]
    for i in xrange(N):
        d[i] = [int(x) for x in finstance.readline().split()]
    c = finstance.readline()
    finstance.close()

    perm = [int(x) for x in fanswer.readline().split()]
    fout.write(processCase(N, d, c, perm) + "\n")

  fout.close()
  fanswer.close()


def processCase(N, d, c, perm):
  if len(perm) != N:
    return "-1"
  v = [0] * N
  prev = 'X'
  count = 0
  for i in xrange(N):
    if v[perm[i]-1] == 1: 
      return "-1"
    v[perm[i]-1] = 1

    cur = c[perm[i]-1]
    if cur == prev:
      count += 1
    else:
      prev = cur
      count = 1

    if count > 3:
      return "-1"

  cost = 0
  for i in xrange(N-1):
    cur = perm[i]-1
    next = perm[i+1]-1

    cost += d[cur][next]

  return str(cost)

ninstances = 495 # default                                                      

if __name__ == '__main__':
  if len(sys.argv) == 3:
    if not os.path.exists(sys.argv[1]):
      print sys.argv[1], "is not a valid path"
    ninstances = int(sys.argv[2])
    input_dir = sys.argv[1]
    if ninstances < 1 or ninstances > 495:
      print "file number should be between 1 and 495 inclusive"
  else:
    print("usage: python scorer_multiple.py [path_of_instance_dir] [num_of_inpu\
t_files]")
    sys.exit(1)
  main(sys.argv[1:])
