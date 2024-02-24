import random
from time import sleep
from collections import Counter

class shotgun():
    def __init__(self):
        self.totShot = random.randint(2,6)
        self.killShot = random.randint(1,self.totShot-1)
        self.blankShot = self.totShot - self.killShot
        self.Chamber = ["KILLSHOT"] * self.killShot + ["BLANKSHOT"] * self.blankShot
        self.sawed = False

        
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
    def __init__(self, health, name):
        self.name = name
        self.hp = health
        self.Inventory = []
        self.isHandcuff = False

    def getHP(self):
        return self.hp


    def playerGetShot(self, gun):
        if gun.sawed == False:
            self.hp = self.hp - 1
        else:
            self.hp = self.hp - 2


    def decision(self):
        sleep(1)
        print("\n1) Shoot opponent")
        print("2) Shoot yourself")
        print("-INVENTORY-")
        self.showInv()
        print()
        user = input("Make your move: ")
        user = user.lower()
        return user


    def shootOpponent(self,player, bullet, gun):
        global currentBulletPosition
        print()
        sleep(0.5)
        print("*c l a c k*")
        sleep(0.5)
        print("*c l a c k*")
        sleep(1)
        if bullet == "KILLSHOT":
            print("\nB A N G ! !")
            player.playerGetShot(gun)
        else:
            print("\n*P L O P*")
            sleep(0.5)
            print("\nNothing happened")
        currentBulletPosition += 1
        gun.sawed = False
        sleep(1)
        showHealthBullet(p1, p2, gun.getTotalShot(), currentBulletPosition)


    def shootYourself(self, bullet, gun):
        global currentBulletPosition
        print()
        sleep(0.5)
        print("*c l a c k*")
        sleep(0.5)
        print("*c l a c k*")
        sleep(1)
        if bullet == "KILLSHOT":
            print("\nB A N G ! !")
            self.playerGetShot(gun)
        else:
            print("\n*P L O P*")
            sleep(0.5)
            print("\nNothing happened")
        currentBulletPosition += 1
        gun.sawed = False
        sleep(1)
        showHealthBullet(p1, p2, gun.getTotalShot(), currentBulletPosition)

    def playerMove(self, nextBullet, opponent, switchTurn, gun):
        global playerTurn
        if not self.isHandcuff:
            
            decide = self.decision()
            if decide == "1":
                self.shootOpponent(opponent, nextBullet, gun)
                playerTurn = switchTurn
                
            elif decide == "2":
                self.shootYourself(nextBullet, gun)
                # ---------- ITEM PART------------
            else: 
                self.useItem(decide, opponent)
        else:
            print(f"{self.name} breaks out of the hand-cuff")
            sleep(0.5)
            self.isHandcuff = False
            playerTurn = switchTurn
        return

# ------------------------------------------------BOT SECTION------------------------------------------------------------
    def botMove(self, nextBullet, opponent, switchTurn, gun):
        global playerTurn, currentBulletPosition
        next = "place holder"
        list = gun.getChamber()
        lastBullet = gun.getTotalShot() - 1
        if not self.isHandcuff:
            print("Bot's Inventory")
            self.showInv()
            print()
            self.botUseItem(gun)

            if gun.hasBullet(currentBulletPosition,gun.getTotalShot()):
                if "Magnifying Glass" in self.Inventory and currentBulletPosition != lastBullet:
                    next = self.useMG(gun)
                    self.Inventory.remove("Magnifying Glass")

                if next == "KILLSHOT":
                    if "Hand-Cuff" in self.Inventory:
                        print("Bot used Hand-Cuff")
                        self.useHandcuff(opponent)
                        self.Inventory.remove("Hand-Cuff")
                    if "Saw" in self.Inventory:
                        print("Bot used Saw")
                        self.useSaw(gun)
                        self.Inventory.remove("Saw")
                    decide = 1
                elif next == "BLANKSHOT":
                    decide = 2
                elif currentBulletPosition == lastBullet:
                    if list[-1] == "KILLSHOT":
                        if "Hand-Cuff" in self.Inventory:
                            print("Bot used Hand-Cuff")
                            self.useHandcuff(opponent)
                            self.Inventory.remove("Hand-Cuff")
                        if "Saw" in self.Inventory:
                            print("Bot used Saw")
                            self.useSaw(gun)
                            self.Inventory.remove("Saw")
                        decide = 1
                    elif list[-1] == "BLANKSHOT" or next == "BLANKSHOT":
                        decide = 2
                else:
                    decide = self.coinFlip()
                sleep(1)
                if decide == 1:
                    print("Bot chose to shoot player")
                    self.shootOpponent(opponent, nextBullet, gun)
                    playerTurn = switchTurn
                else:
                    print("Bot chose to shoot himself")
                    self.shootYourself(nextBullet, gun)
        else:
            print(f"{self.name} breaks out of the hand-cuff")
            sleep(0.5)
            self.isHandcuff = False
            playerTurn = switchTurn
            
        return

    def botUseItem(self, gun):
        sleep(1)
        for i in self.Inventory:
            if i == "Cigar":
                print("Bot used Cigar")
                self.useCigar()
                self.Inventory.remove("Cigar")
            elif i == "Beer":
                print("Bot used Beer")
                self.useBeer(gun)
                self.Inventory.remove("Beer")


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
                print("\nyou dont have this!\n")
                return False

    def useItem(self, decide, opponent):
        if decide == "handcuff" or decide == "hand-cuff" or decide == "hand cuff" and self.itemAvailable("Hand-Cuff"):
            try: self.Inventory.remove("Hand-Cuff")
            except:
                sleep(1)
                print("Item not available")
            else:
                self.useHandcuff(opponent)
        elif decide == "beer" and self.itemAvailable("Beer"):
                try: self.Inventory.remove("Beer") 
                except:
                    sleep(1)
                    print("Item not available")
                else:
                    self.useBeer(gun)
        elif decide == "mg" or decide == "magnifying glass" or decide == "glass" and self.itemAvailable("Magnifying Glass"):
                try: self.Inventory.remove("Magnifying Glass")
                except:
                    sleep(1)
                    print("Item not available")
                else:
                    next_bullet = self.useMG(gun)
                    print(f"\nThe next bullet in the gun is a {next_bullet}\n")
        elif decide == "saw" and self.itemAvailable("Saw"):
                try: self.Inventory.remove("Saw")
                except:
                    sleep(1)
                    print("Item not available")
                else:
                    self.useSaw(gun)
        elif decide == "cigar" or decide == "cig" and self.itemAvailable("Cigar"):
                try: self.Inventory.remove("Cigar")
                except:
                    sleep(1)
                    print("Item not available")
                else:
                    self.useCigar()
        else: 
            print("Enter a valid option\n")

# HAND-CUFF
    def useHandcuff(self, opponent):
        opponent.isHandcuff = True
        print(f"{opponent.name} got hand-cuffed\n")
        sleep(1)

# BEER
    def useBeer(self, gun):
        global currentBulletPosition
        sleep(0.5)
        print(f"\n{self.name} drank a beer and pop out a gun shell")
        print(f"It was a {gun.getChamber()[currentBulletPosition]}\n")
        currentBulletPosition += 1

# MAGNIFYING GLASS
    def useMG(self,gun):
        global currentBulletPosition
        print(f"{self.name} used magnifying glass")
        return gun.getChamber()[currentBulletPosition]
# SAW
    def useSaw(self, gun):
        gun.sawed = True
        sleep(1)
        print(f"{self.name} sawed off the gun")
        print("Now it deal 2 damages")
        print()

# CIGAR
    def useCigar(self):
        self.hp = self.hp + 1
        print(f"{self.name} restores 1 hp\n")



def bothPlayerAlive(p1,p2):
    if p1.getHP() > 0 and p2.getHP() > 0: return True
    return False

def showHealthBullet(p1,p2,totalBullet, currentBulletPosi):
    print(f"\nPLAYER hp: {p1.getHP()}")
    print(f"BOT hp: {p2.getHP()}")
    print(f"Bullet Remaining: {totalBullet - currentBulletPosi}")





# -------------------------------------------ACTUAL GAME HERE------------------------------------------------------------------
# ini the first shotgun cycle
currentBulletPosition = 0
gun = shotgun()
gun.setChamber()
currentChamber = gun.getChamber()

# ini player health 
health = round(gun.getTotalShot()/2)
p1 = Player(health, "NIGGA")
p2 = Player(health, "BOT")

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
        while playerTurn == 1 and gun.hasBullet(currentBulletPosition, gun.getTotalShot()) and bothPlayerAlive(p1,p2):
            print(gun.getChamber())
            print("\n---PLAYER MOVE---")

            p1.playerMove(currentChamber[currentBulletPosition],p2, 2, gun)
            
        
        if not gun.hasBullet(currentBulletPosition, gun.getTotalShot()):
            break

        # ---BOT MOVE---
        while bothPlayerAlive(p1,p2) and playerTurn == 2 and gun.hasBullet(currentBulletPosition, gun.getTotalShot()):
            # print(gun.getChamber())
            print("\n---BOT MOVE---")
            p2.botMove(currentChamber[currentBulletPosition], p1, 1, gun)


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