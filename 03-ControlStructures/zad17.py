# 17.	Let x and y denote the coordinates of a point on the plane. 
# Write a program that determines in which quadrant of the coordinate 
# system the point P (x, y) is located or on which axis it is located, 
# or that it is located in the position (0,0) of the coordinate system.  

x = int(input("x = "))
y = int(input("y = "))

# Center of the coordinate system
if x == 0 and y == 0:
    print(f"Point P({x}, {y}) is at the "
            "center of the coordinate system")
else:
    # X axis
    if x == 0:
        print(f"Point P({x}, {y}) is at the "
                "X axis of the coordinate system")  
    # Y axis
    elif y == 0:
        print(f"Point P({x}, {y}) is at the "
                "Y axis of the coordinate system")
    else:
        # First quadrant of the coordinate system
        if x > 0 and y > 0:
            print(f"Point P({x}, {y}) is in the " 
                    "first quadrant of the coordinate system")
        # Second quadrant of the coordinate system
        elif x < 0 and y > 0:
            print(f"Point P({x}, {y}) is in the " 
                    "second quadrant of the coordinate system")
        # Third quadrant of the coordinate system
        elif x < 0 and y < 0:
            print(f"Point P({x}, {y}) is in the " 
                    "third quadrant of the coordinate system")
        # Fourth quadrant of the coordinate system
        elif x > 0 and y < 0:
            print(f"Point P({x}, {y}) is in the " 
                    "fourth quadrant of the coordinate system")
