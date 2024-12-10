"""write a program that calculates and displays the letter grade for a given numerical score
(Ex A,B,C,D or F ) based on following grading scale:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: 0-59  """

score = int(input("enter the student score:"))
if score >= 90 and score <= 100:
    print("Grade is A", )
elif score >= 80 and score <= 89:
    print("Grade is B")
elif score >= 70 and score <= 79:
    print("Grade is C")
elif score >= 60 and score <= 69:
    print("Grade is D")
elif score >= 100 and score <= -1:
    print("You are a super man ! you cant get a score")
else:
    print("Grade is F")
