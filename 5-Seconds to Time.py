print("Second to Time converter")

while input("If you want quit, write end") != "end" :

    a = int(input("Please enter number you want to convert:"))

    h = a//3600
    if h < 1:
        h == 0

    m = (a-h*3600)//60
    if m < 1:
        m == 0

    s = a - (3600*h + 60*m)

    print ("Your time is", h, " :", m, " :", s)
