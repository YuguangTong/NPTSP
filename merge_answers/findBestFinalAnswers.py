finalans = open("final_answer1.out", "w")
first_answer_in = open("answer1.out", "r")
second_answer_in = open("answer2.out", "r")
first_solution_in = open("score.txt", "r")
second_solution_in = open("score2.txt", "r")

T = 495 # number of files
for t in xrange(0,T):
	c1 = first_solution_in.readline()
	c2 = second_solution_in.readline()
	
	r1 = first_answer_in.readline()
	r2 = second_answer_in.readline()

	if int(c1) > int(c2):
		finalans.write(r2)
	else:
		finalans.write(r1)


