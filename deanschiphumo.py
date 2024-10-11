import math
def calculating_join() :
    y_2 = float(input("coordinate of y of the destination:"))
    y_1 = float(input("enter value of of y of departure point:"))
    d_y = y_2 - y_1
    print(d_y)
    # the difference in the y coordinates of the 2 given points
    x_2 = float(input("enter coordinate of x of the destination point :"))
    x_1 = float(input("enter x coordinate of departure point:"))
    d_x = x_2 - x_1
    print(d_x)
    # the difference in the x coordinates of the 2 given points
    distance = math.sqrt((d_y) ** 2 + (d_x) ** 2)
    print(distance)
    direction =math.degrees( math.atan(d_y / d_x))

    print(direction)
    if d_y < 0 and d_x>0:
       print (direction + 360)
    elif d_x < 0 and d_y>0:
       print (direction + 180)
    elif (d_x and d_y > 0):
       print( direction +  180)
    else:
        print(direction)

calculating_join()





