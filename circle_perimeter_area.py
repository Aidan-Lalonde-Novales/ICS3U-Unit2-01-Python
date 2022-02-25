#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created February 2022
# This program calculates the perimeter and area
# of a circle with a radius of 15mm.

import math


def main():
    # calculates the perimeter and area of the circle
    print("A circle with a radius of 15mm")
    print("will have the following:")
    print("")
    print("Perimeter of {}mm.".format(2 * math.pi * 15))
    print("Area of {}mm².".format(math.pi * 15**2))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
