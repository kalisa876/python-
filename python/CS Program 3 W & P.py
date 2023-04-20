def energy():
    i = 9.81
    mass = float(input("Please enter your body mass in kg: "))
    height = float(input("Please enter your height using a period for inches: "))
    time = float(input("Please enter the amount of time in seconds: "))
    W = (mass * i * height)
    P = (W / time)
    print ("The Work done is" ,W, "and the Power generated is" ,P)
energy()
