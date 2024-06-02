import math
def number_of_can(width, height, coverage):
    number_cans = (width * height) / coverage
    return number_cans
def main():
    width = int(input())
    height = int(input())
    COVERAGE = 5
    num_cans = number_of_can(width, height, COVERAGE)
    print(f"You'll need {math.ceil(num_cans)} cans of paint.")
main()