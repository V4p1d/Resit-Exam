'''
ClassQuestion.py


TOTAL POINTS AVAILABLE: 48


6 points per method. 

--------------------------------------
Marking for methods:
--------------------------------------

6 points -  The program works flawlessly, it is commented and easy to read. The appropriate ideas to solve it, have been used.

5 points - The student has understood the logic and the program works for all inputs.
The code could use some improvement or it is difficult to read and understand. The appropriate ideas to solve the problem have been used.

3-4 points - The student has understood the logic and the program works for most inputs. 
The appropriate ideas to solve the problem have been used.

2 points - The student has understood the logic but there are some major bugs, or the program is incomplete. 
This score is also assigned for programs that execute as intended but in a 
very inefficient way (for instance, using a very long list of if statements 
when the problem could be solved easily with a loop).

1 points -  The student has attempted to solve the exercise but, either there is a 
logical error in the program (e.g., wrote something but it wouldn't solve the problem) 
or the program is largely incomplete.

0 points - The student has not attempted to solve the exercise or missed the point entirely 
(e.g., blank page or solved something unrelated to the question).

'''



# Create a class called Student with fours instance attributes: age, name, mean and subjects. 
# They are created in the constructor. 
#     - 'age' will be an integer
#     - 'name will be a string
#     - 'mean' will be a float always initialised to 0.0
#     - 'subjects' will be an empty dictionary



class Student:

    def __init__(self):
        pass

# Create a method called show. It should:
#   - have one optional parameter, "verbose" set to False by default
#   - when called, if verbose is set to False, it will print on the terminal the name, of the student 
#   - if verbose is set to True, the method show, will print name, age, mean and subjects of the student (for the subjects
#      you will only print the keys, not the items)


    def show(self):
        pass


# Create a method called add_subject. It should:
#   - have 2 parameters: 'subject' and 'grade'
#   - it will add an entry to the dictionary subjects, with 'subject' as key and 'grade' as item
#   - it will automatically update the mean of the student with the new grade. The attribute mean will be equal to the
#     arithmetic mean of all the grades. For example, for a student with subjects = {"computing": 70, "calculus": 90, "physics": 80}
#     mean would be equal to (70 + 90 + 80)/3 = 80

    def add_class(self):
        pass

# Create a method called change_grade. It should:
#   - have 2 parameters: 'subject' and 'grade'
#   - it should change the value of the key 'subject' in the dictionary 'subjects' to 'grade'
#       - if 'class' is not in the dictionary 'subjects' the method will ask the user if they want to add
#         the key 'subject' with item 'grade' to the dictionary 'subjects'. If the user inputs "yes" the new key will
#         be added, otherwise it will not
#   - the value of 'mean' will be automatically updated


    def change_grade(self):
        pass

# Create a method called eliminate_subject. It should:
#   - have 1 parameter: 'subject'
#   - it should eliminate the key 'subject' from the dictionary 'subjects'
#       - if 'subject' is not in the dictionary 'subjects' the method will print "{name} was not enrolled in {subject} "



    def eliminate_subject(self):
        pass

# Write a a new class called "Cohort". The class will have two instance attributes called 'students' and 'mean', 
# created in the constructor.
#   - 'students' will be an empty list.
#   - 'mean' will be a float initialised to 0.0
# The class Cohort will have two methods:
# - one method called "add_student" with one parameter that will add to the list students an object "Student"
# - one method called "compute_average_grade", with a parameter "subject" that will compute the mean of all the grades of the students
#   enrolled in the subject "subject" (this method will ignore the students that are not enrolled in that specific subject)
#       - if no students are enrolled in the subject "subject", the method will return None.



class cohort:

    def __init__(self):
        pass

    def add_student(self):
        pass

    def compute_average_grade(self):
        pass
    