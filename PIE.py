#count the number of possible nonogram grids of nxn sizes for all possible numbers of colors
#export calculations to an excel file for graphing and analyzing

#goals of phase 1:
#1 - configure with github for version control - done!
#2 - determine nessasary code and implement - done!
#3 - configure with excel for data extraction - done!

#phase 2 and beyond - create game to test uniqueness and solvability questions

ListSize =[]
ListColor=[]
ListPossibleBoards=[]
ListX=[]
ListY=[]

import math
import pandas as pd
import decimal

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
   
    calcAllBoards()

#different method of iteration for better use for data extraction
#iterate k through union_size so instead of running 20x20 400 times we only need to once
def PIE_iterator(size, c):
    max=0
    while c<=size+1:
      #  print(c-1)
        f =(union_size(size, c))
     #   print(f)
        add_to_lists(size,c,f)
        c= c +1
        if f>max: 
            max=f
    c=2
    while c<=size+1:  #now that we have the max, we can calculate ListY
        f = (union_size(size,c))
        g = (f/max)*100
        h= convertToScientificNotation(g)
        ListY.append(h)
        c=c+1
    PANDAS(ListSize, ListColor, ListPossibleBoards, ListX, ListY)
    return max

#add values onto lists so PANDAS can put lists in Excel
def add_to_lists(size, c, possibleboards):
    ListSize.append(size)
    ListColor.append(c-1)
    ListPossibleBoards.append(convertToScientificNotation(possibleboards))
    ListX.append(calc_percentage(size, c))

#test lists get data as intended
def test_lists():
    for x in range(len(ListSize)):
        print(ListSize[x])
    for x in range(len(ListColor)):
        print(ListColor[x])
    for x in range(len(ListPossibleBoards)):
        print(ListPossibleBoards[x])
    for x in range(len(ListX)):
        print(ListX[x])
    for x in range(len(ListY)):
        print(ListY[x])

#use pandas to export data to excel
def PANDAS(Size, Colors, PossibleBoards, ColorPercent, BoardPercent):
    dict = {'Size': Size, 'Colors': Colors, 'PossibleBoards': PossibleBoards, 'ColorPercent': ColorPercent, 'BoardPercent': BoardPercent }

    df = pd.DataFrame(dict)

    df.to_excel("PIEoutput.xlsx")

#after all calculations, convert result to scientific notation
#note this does impact accuracy
def convertToScientificNotation(num):
    newNum = decimal.Decimal(num)
    finalNum = format(newNum, '.6e')
    
    return finalNum

#call PIE-iterator 20 times for all nxn boards from n=1 to n=20
def calcAllBoards():
    i=0
    while (i<=20):
        PIE_iterator(i*i, 2)
        i= i+1
        continue


#to run main
if __name__ == "__main__":
    main()

