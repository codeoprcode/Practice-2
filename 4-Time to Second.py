print("Time to second converter")

while 8 == 8:

    h = int(input("Hour: "))
    m = int(input("Miniutes: "))
    s = int(input("Seconds: "))

    print("Your Time is", h,":", m, ":", s)

    sec = h*3600 + m*60 + s

    print("It is ", sec, "seconds")
