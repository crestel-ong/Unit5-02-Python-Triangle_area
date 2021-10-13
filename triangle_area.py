#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Oct 2021
# This Triangle Area program
# This program uses defined functions


def calculate_area_of_triangle(base, height):
    # calculate the area of a triangle

    # process
    area = (base * height) / 2

    # output
    print("")
    print("The area of the triangle is {0} cm².".format(area))


def main():
    # this function gets the base and height

    # input
    base = input("Enter the base length of a triangle (cm): ")
    height = input("Enter the height of a triangle (cm): ")

    try:
        # convert string to integer
        base_from_user = int(base)
        height_from_user = int(height)
        # call functions
        calculate_area_of_triangle(base_from_user, height_from_user)
    except Exception:
        print("Invalid input.")
    print("\nDone.")


if __name__ == "__main__":
    main()
