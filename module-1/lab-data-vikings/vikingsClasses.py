
# Soldier


class Soldier:
    def __init__(self, health, strength):
       self.health = health
       self.strength = strength
    
    def attack(self):
        return self.strength
    
    def receiveDamage(self, damage):
       self.health = self.health - damage


# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):
        super().__init__(health, strength)
        self.name = name
    

    def receiveDamage(self, damage):
        super().receiveDamage(damage)
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"
        else:
            return f"{self.name} has died in act of combat"
    
    def battleCry(self):
        return "Odin Owns You All!"



# Saxon
class Saxon(Soldier):
    
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health = self.health - damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return f"A Saxon has died in combat"

# War
import random 
class War:
    def __init__(self):

        self.vikingArmy = []
        self.saxonArmy =[]

    def addViking(self, Viking):
        
        self.vikingArmy.append(Viking)
    
    def addSaxon(self, Saxon):
        
        self.saxonArmy.append(Saxon)
#testAddSaxon (__main__.TestWar2) ...
#  {'vikingArmy': [<vikingsClasses.Viking object at 0x105efee20>], 
# 'saxonArmy': [<vikingsClasses.Saxon object at 0x105f0e670>]}
    def VikingAttack(self):
        Saxon = Saxon()
        Saxon_random = random.random(self.saxonArmy)

        SaReceiveDamage = Saxon.receiveDamage()
        VikingAttack = Viking.strength()
        SaxonHealth = Saxon.health(self,VikingAttack)
        if Saxon.health < 0:
            self.saxonArmy.remove(Saxon)

    def saxonAttack(self):
        Viking = Viking()
        Viking_random= random.random(self.vikingArmy)
        ViReceiveDamage = Viking.receiveDamage()
        SaxonAttack = Saxon.strength()
        SaxonHealth = Saxon.health(self,VikingAttack)
        if Viking.health < 0:
            self.saxonArmy.remove(Viking)

    def showStatus(self):
        if self.saxonArmy == []:
            return "Vikings have won the war of the century!"
        elif self.vikingArmy == []:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
