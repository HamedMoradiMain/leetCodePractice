x = input(">")
x = [x.strip().lower() for x in x[0:len(x)]]
while True:
    for i in x:
        if i != "y":
            print("good job!")
        if i == "y":
            print("game over!!")
            break
    continue_ = input("do you want to continue: (yes or no)")
    if continue_.lower().strip() == "yes":
        x = input(">")
        pass
    if continue_.lower().strip() == "no":
        break
    