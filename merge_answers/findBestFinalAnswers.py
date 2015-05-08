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
		if int(c2) == -1:  # if invalid, write the other one.
			finalans.write(r1)
		else: #c2 is valid and lower, write r2
			finalans.write(r2)
	else:  # c2 > c1
		if int(c1) == -1: # if invalid, write the other one
			finalans.write(r2)
		else: #c1 is valid and lower, write r1
			finalans.write(r1)


