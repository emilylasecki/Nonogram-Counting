#count the number of possible nonogram grids of multiple colors and variety of sizes
#export calculations to an excel file for graphing and analyzing

#goals of phase 1:
#1 - configure with github for version control
#2 - determine nessasary code and implement
#3 - configure with excel for data extraction

#phase 2 and beyond - create game to test uniqueness and solvability questions

import itertools

#calculates boards. need to implement PIE
def union_size(size, c):
    return c**size

#asks the user for rows, column, and number of colors.
def main():
    print("hello world")
    n = int(input('how many rows does your grid have?\n'))
    m = int(input('how many columns does your grid have? \n'))
    c = int(input('how many colors would you like to test? \n'))
    c += 1
    print(c)
    size = n * m
    print(union_size(size, c))

#to run main
if __name__ == "__main__":
    main()