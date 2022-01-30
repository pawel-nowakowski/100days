from math import ceil

def area_calc(weight, height, area):
    cans = ceil((int(weight) * int(height)) / area)
    print(f'You\'ll need {cans} cans of paint.')

weight_t = input("Type the weight: ")
height_t = input("Type the height: ")
area_coverage = 5
area_calc(weight_t, height_t, area_coverage)
