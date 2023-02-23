def func():
    x1 = int(input("Enter X coordinates of point 1: "))
    y1 = int(input("Enter Y coordinates of point 1: "))
    x2 = int(input("Enter X coordinates of point 2: "))
    y2 = int(input("Enter Y coordinates of point 2: "))
    print("Distance between the points = " , ((x1-x2)**2+(y1-y2)**2)**0.5)

if __name__ == '__main__':
    func()
