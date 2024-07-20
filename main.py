from constraint import *


def main():
    # Create a problem instance
    problem = Problem()

    # Define variables with their domains
    problem.addVariable("x", range(10))  # x can be 0-9
    problem.addVariable("y", range(10))  # y can be 0-9

    # Define constraints
    problem.addConstraint(lambda x, y: x + y == 5)
    problem.addConstraint(lambda x, y: x * y == 6)

    # Find and print solutions
    solutions = problem.getSolutions()

    for solution in solutions:
        print(f"x = {solution['x']}, y = {solution['y']}")


if __name__ == "__main__":
    main()
