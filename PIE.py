#count the number of possible nonogram grids of multiple colors and variety of sizes
#export calculations to an excel file for graphing and analyzing

#goals of phase 1:
#1 - configure with github for version control - done!
#2 - determine nessasary code and implement - done!
#3 - configure with excel for data extraction - current stage

#phase 2 and beyond - create game to test uniqueness and solvability questions

ListSize =[]
ListColor=[]
ListPossibleBoards=[]
ListX=[]
ListY=[]

import math

# method to do bulk calculations
def union_size(size, c):
    max = c**size
    j=1
    i=2
    k=c-1
    total=0
    # controls the "add every other" case
    while (i <c):
        if (i%2 != 0): 
            total = total + ((c-j)**size * factorial_calc(k, (c-i)))
            i = i+1
            j= j+1
            continue
        if (i%2 == 0):
            total = total - (c-j)**size * factorial_calc(k, (c-i))
            i = i+1
            j=j+1
            continue
    # need to add or subtract 1 in all cases depending on what "either or" case we're at
    if (i==c):
        if (c%2 != 0):
            total = total +1
        if (c%2 ==0):
            total = total -1
    return calc_result(c**size, total)

# seperate method to handle final calculations. Possible to build this into the while loops too
def calc_result(max, total):
    result= max + total
    return result

#calculate the binomial coefficents to determine how many times to multiply a certain value 
def factorial_calc(maxc, currentj):
    y= math.comb(maxc, currentj)
    return y

#determine the percentage of possible colors being tested. Final viable color is 100%
def calc_percentage(size, c):
    c= c-1
    return (c/size) *100

#asks the user for rows, column, and number of colors.
def main():
    # print("hello world")
    n = int(input('how many rows does your grid have?\n'))
    m = int(input('how many columns does your grid have? \n'))
    c = int(input('how many colors would you like to test? \n'))
    c= c+1  #1 color needs to run in program as 2
    size = n * m

  #  print(calc_percentage(size, c))
  #  print(union_size(size, c))
    print(PIE_iterator(size, 2))  #currently prints max

#different method of iteration for better use for data extraction
#iterate k through union_size so instead of running 20x20 400 times we only need to once
def PIE_iterator(size, c):
    max=0
    while c<=size+1:
        print(c-1)
        f =(union_size(size, c))
        print(f)
        c= c +1
        if f>max: 
            max=f
    return max #need to calc Y based on this return. new method probably necessary.

def add_to_lists(size, c, possibleboards):
    ListSize.apend(size)
    ListColor.apend(c)
    ListPossibleBoards.apend(possibleboards)
    ListX.apend(calc_percentage(size, c))
    ListY.apend() #possibleboards/max *100

#to run main
if __name__ == "__main__":
    main()

