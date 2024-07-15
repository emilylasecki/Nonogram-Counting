#count the number of possible nonogram grids of multiple colors and variety of sizes
#export calculations to an excel file for graphing and analyzing

#goals of phase 1:
#1 - configure with github for version control - done!
#2 - determine nessasary code and implement - in progress
#3 - configure with excel for data extraction

#phase 2 and beyond - create game to test uniqueness and solvability questions

import itertools
import math

#calculates boards. need to implement PIE
def union_size(size, c):
    max = c**size
    i =2
    j=1
    total =0
    # controls the "add every other" case
    while i <=c:
        if i%2 != 0: 
            # FIXME ((i**size)) needs to be a recursive call, otherwise overcounting
            total = total + ((i**size) * (math.factorial(c)/(math.factorial(j)*(math.factorial(c-j)))))
            print("adding")
            print ((i**size) * (math.factorial(c)/(math.factorial(j)*(math.factorial(c-j)))))
            i = i+1
            j= j+1
        if i%2 == 0:
            total = total - ((i**size) * ((math.factorial(c))/(math.factorial(j) * (math.factorial(c-j)))))
            print("subtracting")
            print ((i**size) * (math.factorial(c)/(math.factorial(j)*(math.factorial(c-j)))))
            i = i+1
            j=j+1
    # need to add or subtract 1 but not in the base case where c=2
    if (i==c) and (c!=2):
        if c%2 != 0:
            total = total -1
        if c%2 ==0:
            total = total +1


    result = max + total
    print("max:")
    print(max)
    print("total to subtract:")
    print(total)

    return result
           

#asks the user for rows, column, and number of colors.
def main():
    print("hello world")
    n = int(input('how many rows does your grid have?\n'))
    m = int(input('how many columns does your grid have? \n'))
    c = int(input('how many colors would you like to test? \n'))
   # c += 1
    print(c)
    size = n * m
    print(union_size(size, c))

#to run main
if __name__ == "__main__":
    main()