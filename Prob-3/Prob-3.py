# Module 3
#   Programming Assignment 4
#     Prob-3.py

# Sam Broyles
def letterGrade(score):
    # your code here
    grade = "F" 
    points = int(input("input score out of 5: "))

    if points == 0:
        print("F")
    elif points == 1:
        print("F")
    elif points == 2:
        print("D")
    elif points == 3:
        print("C")
    elif points == 4:
        print("B")
    elif points == 5:
        print("A")
    else:
        print("invalid grade")

    return grade

def unitTest():
    
    letterGrade(score = 2)

if __name__ == "__main__":
    unitTest()