Y = input()

y = int(Y)

if y % 4 == 0 :
    if y % 100 == 0 :
        if y % 400 == 0 :
            print(1)
        else :
            print(0)
    else :
        print(1)
else :
    print(0)
