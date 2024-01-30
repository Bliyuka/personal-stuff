import random
import time


# class shotgun():
#     def __init__(self):
#         self.totShot = random.randint(2,6)
#         self.killShot = random.randint(1,self.totShot-1)
#         self.blankShot = self.totShot - self.killShot

#     def currentChamber(self):
#         Chamber = ["KILLSHOT"] * self.killShot + ["BLANKSHOT"] * self.blankShot
#         random.shuffle(Chamber)
#         return Chamber

totalShot = random.randint(2,6)
killShot = random.randint(1,totalShot-1)
blankShot = totalShot - killShot

currentMag = ["KILLSHOT"] * killShot + ["BLANKSHOT"] * blankShot
random.shuffle(currentMag)


class Player():
    def shootOpponent(self,opponent_hp, bullet):
        global currentBulletPosition
        print("*clack*\n*clack*")
        if bullet == "KILLSHOT":
            print("BANG!!")
            opponent_hp -= 1
        else:
            print("*P L O P*")
            print("Nothing happened")
        currentBulletPosition += 1
        return opponent_hp

    def shootYourself(self,hp, bullet):
        global currentBulletPosition
        print("*clack*\n*clack*")
        if bullet == "KILLSHOT":
            print("BANG!!")
            hp -= 1
        else:
            print("*P L O P*")
            print("Nothing happened")
        currentBulletPosition += 1
        return hp


    def decision(self):
        print("1) Shoot opponent")
        print("2) Shoot yourself")
        user = int(input("Make your move: "))
        return user


def player1Move(player, next_bullet):
    global again,p1_health, p2_health, playerTurn
    print("\nPLAYER 1 move:")
    decide = player.decision()
    if decide == 1:
        p2_health = player.shootOpponent(p2_health, next_bullet)
        again = False
        playerTurn = 2
    else:
        p1_health = player.shootYourself(p1_health, next_bullet)
    print(f"\nplayer 1 hp: {p1_health}")
    print(f"player 2 hp: {p2_health}")
    return


def player2Move(player, next_bullet):
    global again, p1_health, p2_health, playerTurn
    print("\nPLAYER 2 move:")
    decide = player.decision()
    if decide == 1:
        p1_health = player.shootOpponent(p1_health, next_bullet)
        again = True
        playerTurn = 1
    else:
        p2_health = player.shootYourself(p2_health,next_bullet)
    print(f"\nplayer 1 hp: {p1_health}")
    print(f"player 2 hp: {p2_health}")
    return

# actual game here
currentBulletPosition = 0
print(f"\neach player has {round(totalShot/2)} hp")
print("whoever out of lives first loses")
p1_health = round(totalShot/2)
p2_health = p1_health

print(f"\nThere are {totalShot} shots: {killShot} deadly shot(s) and {blankShot} blank shot(s)")

p1 = Player()
p2 = Player()

playerTurn = 1

again = True
while p1_health > 0 and p2_health > 0:
    while currentBulletPosition <= len(currentMag)-1 and p1_health > 0 and p2_health > 0:
        while again and p1_health > 0 and playerTurn == 1:
            player1Move(p1, currentMag [currentBulletPosition])
            print(f"Bullet Remaining: {len(currentMag) - currentBulletPosition}")

        if currentBulletPosition > len(currentMag)-1:
            break
        while not again and p1_health > 0 and p2_health > 0 and playerTurn == 2:
            if currentBulletPosition > len(currentMag)-1:
                break
            else:
                player2Move(p2, currentMag[currentBulletPosition])
                print(f"Bullet Remaining: {len(currentMag) - currentBulletPosition}")

    if currentBulletPosition >= len(currentMag)-1:
        again = True
        currentBulletPosition = 0
        totalShot = random.randint(2,6)
        killShot = random.randint(1,totalShot-1)
        blankShot = totalShot - killShot

        currentMag = ["KILLSHOT"] * killShot + ["BLANKSHOT"] * blankShot
        random.shuffle(currentMag)

        print("\n\nOut of ammo")
        print("R E L O A D")
        print(f"\nThere are {totalShot} shots: {killShot} deadly shot(s) and {blankShot} blank shot(s)")

    else:
        break
print("We have a loser")