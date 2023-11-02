import random
n = random.randint(4,31)
print("Число камней в куче: ",n)
while n > 0:
    us = int(input("Сколько камней возьмём? "))
    if (us<1) or (us>3):        
        print("Неверное количество камней ")
        break
    else:
        n -= us
        if n == 1:
            print("ПОБЕДА!")
            exit()
        n= n - random.randint(1,4)
        print("Камней в куче после хода соперника: ", n)
        if n == 1:
            print("ПОРАЖЕНИЕ((")
            exit()
