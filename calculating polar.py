import math


def calculating_polar():
    y = float(input("enter y coordinate of origin point:"))
    x = float(input("enter x coordinate of origin point:"))
    distance = float(input("enter distance between origin and point of intrest:"))
    direction = float(input("enter direction of point of intrest from origin:"))
    # calculating y coordinate of point of intrest,y1
    y1 = y + distance * math.sin(direction)
    # calculating x coordinate of point of intrest,x1
    x1 = x + distance * math.cos(direction)
    print(y)
    print(x)


calculating_polar()

