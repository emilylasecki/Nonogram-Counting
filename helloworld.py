#count the number of possible nonogram grids of multiple colors and variety of sizes
#export calculations to an excel file for graphing and analyzing

#goals of phase 1:
#1 - configure with github for version control
#2 - determine nessasary code and implement
#3 - configure with excel for data extraction

#phase 2 and beyond - create game to test uniqueness and solvability questions

import itertools

def union_size(sets):
    i = 1
    subset =4
    return sum((-1)**(i+1)) * len(set.intersection(*subset))


def main():
    print("hello world")