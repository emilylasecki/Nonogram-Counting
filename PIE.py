#count the number of possible nonogram grids of multiple colors and variety of sizes
#export calculations to an excel file for graphing and analyzing

#goals of phase 1:
#1 - configure with github for version control - done!
#2 - determine nessasary code and implement - in progress
#3 - configure with excel for data extraction

#phase 2 and beyond - create game to test uniqueness and solvability questions

import itertools
import math
import sys

j=0
i=2
total=0

def union_size(size, c):
    max = c**size
    sys.stdout.write("max is: ")
    print(max)
    global total
    global i
    global j
    #j=c
    # base case
    # controls the "add every other" case
    while i <=c:
        if (c==i):
            sys.stdout.write("base case activated and it is: ")
            print(c**size)
            #return c**size
        if i%2 != 0: 
            # FIXME ((i**size)) needs to be a recursive call, otherwise overcounting
            # ^-- input but not opperating as intended
            i = i+1
            j= j+1
            total = total + (union_size(size, j) * (math.factorial(c)/(math.factorial(j)*(math.factorial(c-j)))))
            sys.stdout.write("adding: ")
            print ((i**size) * (math.factorial(c)/(math.factorial(j)*(math.factorial(c-j)))))
            continue
        if i%2 == 0:
            i = i+1
            j= j+1
            total = total - ((union_size(size, j)) * ((math.factorial(c))/(math.factorial(j) * (math.factorial(c-j)))))
            sys.stdout.write("subtracting: ")
            print ((i**size) * (math.factorial(c)/(math.factorial(j)*(math.factorial(c-j)))))
            continue
        
    # need to add or subtract 1 but not in the base case where c=2
    if (i==c) and (c!=2):
        if c%2 != 0:
            total = total -1
        if c%2 ==0:
            total = total +1


    result = max - total
    sys.stdout.write("max: ")
    print(max)
    sys.stdout.write("total to subtract: ")
    print(total)
    print(result)

    return result
           

#asks the user for rows, column, and number of colors.
def main():
    print("hello world")
    n = int(input('how many rows does your grid have?\n'))
    m = int(input('how many columns does your grid have? \n'))
    c = int(input('how many colors would you like to test? \n'))
    # consider adding 1 to colors to make more sense with logic
    print(c)
    size = n * m
    print(union_size(size, c))

#to run main
if __name__ == "__main__":
    main()