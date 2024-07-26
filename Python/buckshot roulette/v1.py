import random
import time

totalShot = random.randint(2,6)
killShot = random.randint(1,totalShot-1)
blankShot = totalShot - killShot

currentMag = ["KILLSHOT"] * killShot + ["BLANKSHOT"] * blankShot
random.shuffle(currentMag)

# def shootOrNot(choice):
#     if choice == "y":        

# while totalShot > 0:
# print(f"The gun has {killShot} shot and {blankShot} blank")


print(currentMag)
print(f"\neach player has {round(totalShot/2)} hp")
print("who has higher hp at the end wins")
print("(dont ask me why im lazy)")
p1_health = totalShot/2
p2_health = totalShot/2

print(f"\nThere are {totalShot} shots: {killShot} deadly shot(s) and {blankShot} blank shot(s)")

i = 0
while i < len(currentMag):
    # print(i)
    again = True
    while again:
        print("\n--PLAYER 1 move:")
        print("1) Shoot PLAYER 2")
        print("2) Shoot yourself")
        p1 = int(input("Make your move: "))
        print()
        time.sleep(1)
        print("*clack*")
        # time.sleep(1)
        print("*clack\n")
        if p1 == 1:
            if currentMag[i] == "KILLSHOT":
                time.sleep(1)
                print("*BANG!*\n")
                p2_health -= 1
            else:
                time.sleep(1)
                print("*plop*\n")
                print("nothing happened\n")
            again = False
        elif p1 == 2:
            if currentMag[i] == "KILLSHOT":
                time.sleep(1)
                print("BANG!\n")
                p1_health -= 1
            else:
                time.sleep(1)
                print("*plop*\n")
                print("nothing happened\n")
                time.sleep(0.5)
                print("the next move is yours\n")
        i += 1
                  
    if i == len(currentMag):
        break
    else:
        again = True
        while again:
            print("--PLAYER 2 move:")
            print("1) Shoot PLAYER 1")
            print("2) Shoot yourself")
            p2 = int(input("Make your move: "))
            time.sleep(1)
            print("*clack*")
            # time.sleep(1)
            print("*clack*\n")
            if p2 == 1:
                if currentMag[i] == "KILLSHOT":
                    time.sleep(1)
                    print("*BANG!*\n")
                    p2_health -= 1
                else:
                    time.sleep(1)
                    print("*plop*\n")
                    print("nothing happened\n")
                again = False
            elif p2 == 2:
                if currentMag[i] == "KILLSHOT":
                    time.sleep(1)
                    print("BANG!\n")
                    p1_health -= 1
                else:
                    time.sleep(1)
                    print("*plop*\n")
                    print("nothing happened\n")
                    time.sleep(0.5)
                    print("the next move is yours\n")
            i += 1

print(f"player 1 hp: {round(p1_health)}")
print(f"player 2 hp: {round(p2_health)}")
