import random
import time


class shotgun():
    def __init__(self):
        self.totShot = random.randint(2,6)
        self.killShot = random.randint(1,self.totShot-1)
        self.blankShot = self.totShot - self.killShot
        # self.Chamber = random.shuffle(["KILLSHOT"] * self.killShot + ["BLANKSHOT"] * self.blankShot)
        
    def getTotalShot(self):
        return self.totShot
    
    def getKillShot(self):
        return self.killShot
    
    def getBlankShot(self):
        return self.blankShot
    
    def getChamber(self):
        list = ["KILLSHOT"] * self.killShot + ["BLANKSHOT"] * self.blankShot
        random.shuffle(list)
        return list
    
    def reload(self):
        time.sleep(0.5)
        print("\n\nOut of ammo")
        time.sleep(0.5)
        print("\nR E L O A D")
        time.sleep(0.5)
        print(f"\nThere are {gun.getTotalShot()} shots: {gun.getKillShot()} deadly shot(s) and {gun.getBlankShot()} blank shot(s)")


# totalShot = random.randint(2,6)
# killShot = random.randint(1,totalShot-1)
# blankShot = totalShot - killShot

# currentMag = ["KILLSHOT"] * killShot + ["BLANKSHOT"] * blankShot
# random.shuffle(currentMag)


class Player():
    def shootOpponent(self,opponent_hp, bullet):
        global currentBulletPosition
        print()
        time.sleep(0.5)
        print("*c l a c k*")
        time.sleep(0.5)
        print("*c l a c k*")
        time.sleep(1)
        if bullet == "KILLSHOT":
            print("\nBANG!!")
            opponent_hp -= 1
        else:
            print("\n*P L O P*")
            time.sleep(0.5)
            print("\nNothing happened")
        currentBulletPosition += 1
        time.sleep(1)
        return opponent_hp

    def shootYourself(self,hp, bullet):
        global currentBulletPosition
        print()
        time.sleep(0.5)
        print("*c l a c k*")
        time.sleep(0.5)
        print("*c l a c k*")
        time.sleep(1)
        if bullet == "KILLSHOT":
            print("\nBANG!!")
            hp -= 1
        else:
            print("\n*P L O P*")
            time.sleep(0.5)
            print("\nNothing happened")
        currentBulletPosition += 1
        time.sleep(1)
        return hp


    def decision(self):
        print("1) Shoot opponent")
        print("2) Shoot yourself")
        user = int(input("Make your move: "))
        return user

def player1Move(player, next_bullet,a,currentBulletPosition):
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
    print(f"Bullet Remaining: {a - currentBulletPosition -1}")
    return

def player2Move(player, next_bullet, a, currentBulletPosition):
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
    print(f"Bullet Remaining: {a - currentBulletPosition -1}")
    return


# -------------------------------------------actual game here-------------------------------------------

gun = shotgun()
currentChamber = gun.getChamber()
currentBulletPosition = 0


print(f"\neach player has {round(gun.getTotalShot()/2)} hp")
print("whoever out of lives first loses")

p1_health = round(gun.getTotalShot()/2)
p2_health = p1_health

# p1_health = 10
# p2_health = p1_health

print(f"\nThere are {gun.getTotalShot()} shots: {gun.getKillShot()} deadly shot(s) and {gun.getBlankShot()} blank shot(s)")

p1 = Player()
p2 = Player()

playerTurn = 1

while p1_health > 0 and p2_health > 0:
    a = len(currentChamber)
    while currentBulletPosition <= len(currentChamber)-1 and p1_health > 0 and p2_health > 0:
        while p1_health > 0 and playerTurn == 1:
            player1Move(p1, currentChamber[currentBulletPosition],a,currentBulletPosition)
            

        if currentBulletPosition > len(currentChamber)-1:
            break
        while p1_health > 0 and p2_health > 0 and playerTurn == 2:
            if currentBulletPosition > len(currentChamber)-1:
                break
            else:
                player2Move(p2, currentChamber[currentBulletPosition],a,currentBulletPosition)

    if currentBulletPosition > len(currentChamber)-1 and p1_health > 0 and p2_health > 0:
        currentBulletPosition = 0
        gun = shotgun()
        currentChamber = gun.getChamber()
        gun.reload()
    else:
        break
print("\nWe have a loser")