import math

floor_length = input("enter floor length: ")
floor_width = input("enter the width of the floor: ")
panel_length = input("enter panel length: ")
panel_width = input("enter the width of the panel: ")
panels_package = input("enter the number of panels in the package: ")

floor_area = float(floor_width) * float(floor_length)
panel_area = float(panel_length) * float(panel_width)


def panel_calc():
    return math.ceil(((floor_area * 1.1)/panel_area)/int(panels_package))


print("You need : " + str(panel_calc()))
