# Module 3
#   Programming Assignment 4
#     Prob-5.py

# Sam Broyles

def main():
    try:
        x = eval(2)
        print("x:", x)
    except TypeError:
        print("variable 'x' must be a string")
    except:
        print("unknown exception")

main()
    