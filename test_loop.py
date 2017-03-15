while True:
    sys=input("Enter (q) to quet or (c) to continue;")
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


    
    

