import random
from time import sleep
from collections import Counter

class shotgun():
    def __init__(self):
        self.totShot = random.randint(2,6)
        self.killShot = random.randint(1,self.totShot-1)
        self.blankShot = self.totShot - self.killShot
        self.Chamber = ["KILLSHOT"] * self.killShot + ["BLANKSHOT"] * self.blankShot

        
    def getTotalShot(self):
        return self.totShot
    
    def getKillShot(self):
        return self.killShot
    
    def getBlankShot(self):
        return self.blankShot

    def setChamber(self):
        random.shuffle(self.Chamber)

    def getChamber(self):
        return self.Chamber
    
    
    def reload(self):
        sleep(0.5)
        print("\n\nOut of ammo")
        sleep(0.5)
        print("\nR E L O A D")
        sleep(0.5)
        print(f"\nThere are {gun.getTotalShot()} shots: {gun.getKillShot()} deadly shot(s) and {gun.getBlankShot()} blank shot(s)")
        
    def hasBullet(self, currentBulletPosition, totalBullet):
        if currentBulletPosition >= totalBullet: return False
        return True



class Player():
    def __init__(self, health):
        self.hp = health
        self.Inventory = []

    def getHP(self):
        return self.hp


    def playerGetShot(self):
        self.hp = self.hp - 1


    def decision(self):
        sleep(1)
        print("1) Shoot opponent")
        print("2) Shoot yourself")
        print("\n---INVENTORY---")
        self.showInv()
        print()
        user = input("Make your move: ")
        user = user.lower()
        return user


    def shootOpponent(self,player, bullet):
        global currentBulletPosition
        print()
        sleep(0.5)
        print("*c l a c k*")
        sleep(0.5)
        print("*c l a c k*")
        sleep(1)
        if bullet == "KILLSHOT":
            print("\nB A N G ! !")
            player.playerGetShot()
        else:
            print("\n*P L O P*")
            sleep(0.5)
            print("\nNothing happened")
        currentBulletPosition += 1
        sleep(1)


    def shootYourself(self, player, bullet):
        global currentBulletPosition
        print()
        sleep(0.5)
        print("*c l a c k*")
        sleep(0.5)
        print("*c l a c k*")
        sleep(1)
        if bullet == "KILLSHOT":
            print("\nB A N G ! !")
            player.playerGetShot()
        else:
            print("\n*P L O P*")
            sleep(0.5)
            print("\nNothing happened")
        currentBulletPosition += 1
        sleep(1)

    def playerMove(self, nextBullet, opponent, switchTurn):
        global playerTurn
        while True:
            decide = self.decision()
            if decide == "1":
                self.shootOpponent(opponent, nextBullet)
                playerTurn = switchTurn
                break
            elif decide == "2":
                self.shootYourself(self, nextBullet)
                
            # ---------- ITEM PART------------
            elif decide == "handcuff" or decide == "hand-cuff" or decide == "hand cuff" and self.itemAvailable("Hand-Cuff"):
                    print("handcuff test\n")
            elif decide == "beer" and self.itemAvailable("Beer"):
                
                    print("beer test\n")
            elif decide == "mg" or decide == "magnifying glass" or decide == "glass" and self.itemAvailable("Magnifying Glass"):
                
                    print("glass test\n")
            elif decide == "saw" and self.itemAvailable("Saw"):
                
                    print("saw test\n")
            elif decide == "cigar" or decide == "cig" and self.itemAvailable("Cigar"):
                
                    print("cigar test\n")
            else:
                print("Enter a valid option!\n")
        return

# ------------------------------------------------BOT SECTION------------------------------------------------------------
    def botMove(self, nextBullet, opponent, switchTurn, gun):
        global playerTurn
        print("Bot's Inventory")
        self.showInv()
        print()
        list = gun.getChamber()
        if list[-1] == "KILLSHOT":
            decide = 1
        elif list[-1] == "BLANKSHOT":
            decide = 2
        else:
            decide = self.coinFlip()
        sleep(1)
        if decide == 1:
            print("Bot chose to shoot player")
            self.shootOpponent(opponent, nextBullet)
            playerTurn = switchTurn
        else:
            print("Bot chose to shoot himself")
            self.shootYourself(self, nextBullet)
        return

    def coinFlip(self):
        return random.randint(1,2)
        

# ------------------------------------------------ITEM SECTION------------------------------------------------------------
# give items
    def giveItem(self):
        sleep(0.5)
        noOfItem = random.randint(1,3)
        print(f"Get {noOfItem} item(s):")
        for i in range(noOfItem):
            sleep(0.5)
            item = random.randint(1,5)
            if item == 1:
                self.Inventory.append("Hand-Cuff")
                print("Hand-Cuff added")
            elif item == 2:
                self.Inventory.append("Beer")
                print("Beer added")
            elif item == 3:
                self.Inventory.append("Magnifying Glass")
                print("Magnifying Glass added")
            elif item == 4:
                self.Inventory.append("Saw")
                print("Saw added")
            elif item == 5:
                self.Inventory.append("Cigar")
                print("cigarette added")

# show Inventory
    def showInv(self):
        counted_items = Counter(self.Inventory)
        duplicates = {item: count for item, count in counted_items.items() if count >= 1}
        print(duplicates)

# Item check available
    def itemAvailable(self, item):
            if item in self.Inventory:
                return True
            else:
                print("you dont have this!\n")
                return False


# HAND-CUFF
    # def useHandcuff(self):
        
# BEER

# MAGNIFYING GLASS

# SAW

# CIGAR




def bothPlayerAlive(p1,p2):
    if p1.getHP() > 0 and p2.getHP() > 0: return True
    return False

def showHealthBullet(p1,p2,totalBullet, currentBulletPosition):
    print(f"\nPLAYER hp: {p1.getHP()}")
    print(f"BOT hp: {p2.getHP()}")
    print(f"Bullet Remaining: {totalBullet - currentBulletPosition}")





# -------------------------------------------ACTUAL GAME HERE------------------------------------------------------------------
# ini the first shotgun cycle
gun = shotgun()
gun.setChamber()
currentChamber = gun.getChamber()
currentBulletPosition = 0

# ini player health 
health = round(gun.getTotalShot()/2)
p1 = Player(health)
p2 = Player(health)

# announce player hp and gun shots
print(f"\neach player has {round(gun.getTotalShot()/2)} hp")
print("whoever out of lives first loses")

sleep(1)
print(f"\nThere are {gun.getTotalShot()} shots: {gun.getKillShot()} deadly shot(s) and {gun.getBlankShot()} blank shot(s)")


# the game begins
playerTurn = 1
while bothPlayerAlive(p1,p2):
    sleep(1)
    print("\n- Player:")
    p1.giveItem()
    sleep(1)
    print("\n- Bot:")
    p2.giveItem()
    # ---PLAYER MOVE---
    sleep(1)
    while gun.hasBullet(currentBulletPosition, gun.getTotalShot()) and bothPlayerAlive(p1,p2):
        while playerTurn == 1 and gun.hasBullet(currentBulletPosition, gun.getTotalShot()):
            # print(gun.getChamber())
            print("\n---PLAYER MOVE---")
            p1.playerMove(currentChamber[currentBulletPosition],p2, 2)
            showHealthBullet(p1, p2, gun.getTotalShot(), currentBulletPosition)
        
        if not gun.hasBullet(currentBulletPosition, gun.getTotalShot()):
            break

        # ---BOT MOVE---
        while bothPlayerAlive(p1,p2) and playerTurn == 2 and gun.hasBullet(currentBulletPosition, gun.getTotalShot()):
            # print(gun.getChamber())
            print("\n---BOT MOVE---")
            p2.botMove(currentChamber[currentBulletPosition], p1, 1, gun)
            showHealthBullet(p1, p2, gun.getTotalShot(), currentBulletPosition)

    # --- RELOAD if both player alive---
    if not gun.hasBullet(currentBulletPosition, gun.getTotalShot()) and bothPlayerAlive(p1,p2):
        currentBulletPosition = 0
        gun = shotgun()
        gun.setChamber()
        currentChamber = gun.getChamber()
        gun.reload()

    else:
        break

print("\nWe have a loser")