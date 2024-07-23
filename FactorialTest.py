import math

def main():
    x= math.factorial(56)
    y= math.factorial(27)
    z = math.factorial(56-27)

    a= (x / (y *z))

    print("56 choose 27 is")
    print(a)

    b= math.factorial(58)
    c= math.factorial(27)
    d = math.factorial(58-27)
    print("b:")
    print(b)
    print("c:")
    print(c)
    print("d:")
    print(d)

    e= (b / (c *d)) #this is where we lose accuracy

    print("58 choose 27 is")
    print(e)
    f= math.comb(58, 27)

    print(f)


#to run main
if __name__ == "__main__":
    main()