'''
GeneralProgramming.py



Functions performing operations on basic Python data structures.

TOTAL POINTS AVAILABLE: 40 (notice that each exercise has its own weight, specified under the examples)


1 * weight points -  The program works flawlessly and the appropriate ideas to solve it, have been used.

0.75 * weight points - The student has understood the logic and the program works for most inputs.
The code could use some improvement or it is very hard to read. The appropriate ideas to solve the problem have been used.

0.5 * weight points - The student has understood the logic but there are some major bugs, or the program is incomplete. 
This score is also assigned for programs that execute as intended but in a 
very inefficient way (for instance, using a very long list of if statements 
when the problem could be solved easily with a loop).

0.25 * weight points -  The student has attempted to solve the exercise but, either there is a 
logical error in the program (e.g., wrote something but it wouldn't solve the problem) 
or the program is largely incomplete.

0 points - The student has not attempted to solve the exercise or missed the point entirely 
(e.g., blank page or solved something unrelated to the question).
'''
# In a Pascal triangle, each number is the sum of the two numbers directly above it. For example 
#                      1
#                    1   1
#                  1   2   1
#                1   3   3   1
#              1   4   6   4   1
# Write a function that, given an integet m, returns the first m rows of the pascal triangle as a list of lists.
# For example:
# m = 5
# output = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

def pascalTriangle():
    return