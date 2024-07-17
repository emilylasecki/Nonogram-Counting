#count the number of possible nonogram grids of multiple colors and variety of sizes
#export calculations to an excel file for graphing and analyzing

#goals of phase 1:
#1 - configure with github for version control - done!
#2 - determine nessasary code and implement - in progress
#3 - configure with excel for data extraction

#phase 2 and beyond - create game to test uniqueness and solvability questions

import itertools
import math

total=0
def union_size(size, c, i):
    max = c**size
    j=1
    global total
    # controls the "add every other" case
    while (i <=c):
        #base case
        if (c==i):  #isn't base case when i == 2???
            print("base case activated")  #need to include another method here, sometimes this is called when shouldn't
            return c**size + total
           # return calc_result(c**size, total) # placeholder, while loop should be the one to return
        if (i%2 != 0): 
            max_val = union_size(size, c, i+1) #recursive element
            total = total + (max_val * factorial_calc(c, j))
            print("adding")
            print (max_val * factorial_calc(c, j))
           # print("current total")
           # print(total)
            i = i+1
            j= j+1
            continue
        if (i%2 == 0):
            max_val = union_size(size, c, i+1)
            total = total - max_val * factorial_calc(c, j)
            print("subtracting")
            print (max_val * factorial_calc(c, j))
            i = i+1
            j=j+1
    # need to add or subtract 1 but not in the base case where c=2 -LIES we could 15 valid boards, blank board is not valid
    if (i==c) and (c!=2):
        if (c%2 != 0):
            total = total -1
            print("subtracting 1")
        if (c%2 ==0):
            total = total +1
            print("adding 1")
 #   return calc_result(c**size, total)


# need to have a seperate method handle the final calculations -MORE LIES!!! its better to include in base case
def calc_result(max, total):
    print("recursion over, answer: ")
    result= max +total
    return result

#calculate the binomial coefficents to determine how many times to multiply a certain value FIXME confirm calcs correct value
def factorial_calc(maxc, currentj):
    return ((math.factorial(maxc))/(math.factorial(currentj) * (math.factorial(maxc-currentj))))

#asks the user for rows, column, and number of colors.
def main():
    print("hello world")
    n = int(input('how many rows does your grid have?\n'))
    m = int(input('how many columns does your grid have? \n'))
    c = int(input('how many colors would you like to test? \n'))
   # c += 1 add back at the end
   # c += 1
    print(c)
    size = n * m
    print(union_size(size, c, 2))


#to run main
if __name__ == "__main__":
    main()