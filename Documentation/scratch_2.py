def board(height, width):
    x = "--- " * width
    y = "|  " * (height + 1)

    for i in range (0, height):
        print(x)
        print(y)

heightinput = int(input("Enter the height: "))
widthinput = int(input("Enter the width: "))

board(heightinput, widthinput)
