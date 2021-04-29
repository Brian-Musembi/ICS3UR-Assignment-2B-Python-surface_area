#!/usr/bin/env python3

# Created by: Brian Musembi
# Created on: 29 April 2021
# This program calculates the surface area of a square-based pyramid
#     where the user gets to enter the base, height mm

import math


def main():
    # main function

    print("Let's calculate the surface area of a square pyramid. ")
    print("")

    # input
    base = int(input("Enter the base length (m): "))
    height = int(input("Enter the height (m): "))

    # process
    surface_area = (base * base) + (base + base) * math.sqrt(((
        base * base) / 4) + (height * height))
    print("")

    # output
    print("The surface area is {} m²".format(surface_area))


if __name__ == "__main__":
    main()
