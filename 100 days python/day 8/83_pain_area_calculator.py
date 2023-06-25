import math

def paint_calc(height,width,cover):
    no_of_cans=(test_h*test_w)/coverage
    round_up_cans = math.ceil(no_of_cans)

    print(f"You'll need {round_up_cans} cans of paint.")
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
#round-->The math.ceil (ceiling) function returns the smallest integer higher or equal to x.

