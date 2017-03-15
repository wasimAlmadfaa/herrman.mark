while True:
    sys=input("Enter (q) to the next game(c) to continue;")
    if sys == "q":
        print("XXXXXXXXXXXX")
        break
    rows=int(input("Enter who many rows you wont;"))
    cols=int(input("Enter who many rows you wont;"))

    for i in range(rows):
        for x in range(cols):
            print("*" , end="")

        print()
    if i == rows and x == cols:
        break
while True:
    sys=input("Enter (q) to quet or (c) to go to the next game;")
    if sys == "q":
        print("XXXXXXXXXXXX")
        break
    r=int(input("Enter who many rows you wont;"))
    for i in range(r):
        for x in range(i+1):
            print("*" , end="")

        print()
    if i == r:
        break
    
    

