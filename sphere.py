# sphere.py
# Created on 12/10/18 by Jenna Folsom
# A program to calculate the volume and surface area of a sphere from its radius

def main():

    import math
    
    # this is an introduction
    print("This program is used to calculate the volume and surface area of a sphere from its radius.")

    # this is an input
    radius = eval(input("Enter the radius of the sphere: "))
    volume = 4 / 3 * math.pi * radius ** 3
    surface = 4 * math.pi * radius ** 2

    # this is an output
    print("The volume of the sphere is", volume, ".")
    print("The surface area of the sphere is", surface, ".")

main()
