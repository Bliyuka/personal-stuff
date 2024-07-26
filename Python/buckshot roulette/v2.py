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
        
    def hasBullet(self, currentBulletPosition, totalBullet):
        if currentBulletPosition >= totalBullet: return False
        return True

class Player():
    def __init__(self, health):
        self.hp = health


    def getHP(self):
        return self.hp


    def playerGetShot(self):
        self.hp = self.hp - 1


    def shootOpponent(self,player, bullet):
        global currentBulletPosition
        print()
        time.sleep(0.5)
        print("*c l a c k*")
        time.sleep(0.5)
        print("*c l a c k*")
        time.sleep(1)
        if bullet == "KILLSHOT":
            print("\nB A N G ! !")
            player.playerGetShot()
        else:
            print("\n*P L O P*")
            time.sleep(0.5)
            print("\nNothing happened")
        currentBulletPosition += 1
        time.sleep(1)


    def shootYourself(self, player, bullet):
        global currentBulletPosition
        print()
        time.sleep(0.5)
        print("*c l a c k*")
        time.sleep(0.5)
        print("*c l a c k*")
        time.sleep(1)
        if bullet == "KILLSHOT":
            print("\nB A N G ! !")
            player.playerGetShot()
        else:
            print("\n*P L O P*")
            time.sleep(0.5)
            print("\nNothing happened")
        currentBulletPosition += 1
        time.sleep(1)


    def decision(self):
        print("1) Shoot opponent")
        print("2) Shoot yourself")
        user = int(input("Make your move: "))
        return user


    def playerMove(self, nextBullet, opponent, switchTurn):
        global playerTurn
        decide = self.decision()
        if decide == 1:
            self.shootOpponent(opponent, nextBullet)
            playerTurn = switchTurn
        else:
            self.shootYourself(self, nextBullet)
        return

def bothPlayerAlive(p1,p2):
    if p1.getHP() > 0 and p2.getHP() > 0: return True
    return False

def showHealthBullet(p1,p2,totalBullet, currentBulletPosition):
    print(f"\nplayer 1 hp: {p1.getHP()}")
    print(f"player 2 hp: {p2.getHP()}")
    print(f"Bullet Remaining: {totalBullet - currentBulletPosition}")


# -------------------------------------------actual game here-------------------------------------------
# ini the first shotgun cycle
gun = shotgun()
currentChamber = gun.getChamber()
currentBulletPosition = 0
# ini player health 
health = round(gun.getTotalShot()/2)
p1 = Player(health)
p2 = Player(health)

# announce player hp and gun shots
print(f"\neach player has {round(gun.getTotalShot()/2)} hp")
print("whoever out of lives first loses")
print(f"\nThere are {gun.getTotalShot()} shots: {gun.getKillShot()} deadly shot(s) and {gun.getBlankShot()} blank shot(s)")

playerTurn = 1
while bothPlayerAlive(p1,p2):
    while gun.hasBullet(currentBulletPosition, gun.getTotalShot()) and bothPlayerAlive(p1,p2):
        while playerTurn == 1 and gun.hasBullet(currentBulletPosition, gun.getTotalShot()):
            print("\n---PLAYER 1 MOVE---")
            p1.playerMove(currentChamber[currentBulletPosition],p2, 2)
            showHealthBullet(p1, p2, gun.getTotalShot(), currentBulletPosition)
        
        if not gun.hasBullet(currentBulletPosition, gun.getTotalShot()):
            break
        
        while bothPlayerAlive(p1,p2) and playerTurn == 2 and gun.hasBullet(currentBulletPosition, gun.getTotalShot()):
            print("\n---PLAYER 2 MOVE---")
            p2.playerMove(currentChamber[currentBulletPosition], p1, 1)
            showHealthBullet(p1, p2, gun.getTotalShot(), currentBulletPosition)
    
    if not gun.hasBullet(currentBulletPosition, gun.getTotalShot()) and bothPlayerAlive(p1,p2):
        currentBulletPosition = 0
        gun = shotgun()
        currentChamber = gun.getChamber()
        gun.reload()
    
    else:
        break

print("\nWe have a loser")