import math

class Army:
    def __init__(self, units=[]):
        self.units = []
    
    def add_units(self, unit_type, amount):
        for i in range(amount):
            self.units.append(unit_type())
    
    def sort_units(self):

        can_move = False
        units = self.units

        for i in units:
            if type(i) == Warlord:
                can_move = True
                break
    
        if can_move and len(units) > 1:
            for i in range(len(units)):
                if type(units[i]) == Warlord:
                    units.append(units[i])
                    units[i] = 0
            
            lancers = 0
            for i in range(len(units)):
                if type(units[i]) == Lancer:
                    units.insert(0, units[i])
                    units[i+1] = 0
                    lancers += 1
            if lancers == 0:
                for i in range(len(units)):
                    if type(units[i]) in (Warrior, Knight, Defender, Vampire, Rookie):
                        units.insert(0, units[i])
                        units[i+1] = 0
            for i in range(len(units)):
                if type(units[i]) == Healer:
                    units.insert(1, units[i])
                    units[i+1] = 0
            
            while 0 in units:
                units.remove(0)
        

'''
UNIT TYPES
'''
class Warrior:
    def __init__(self):
        self.health = 50
        self.attack = 5

    def hit(self, enemy):
        vampirism = False
        defense = 0
        max_health = None
        try:
            vampirism = self.vampirism
        except:
            pass
        try:
            max_health = self.max_health
        except:
            pass
        try:
            defense = enemy.defense
        except:
            pass
        enemy.health = enemy.health + min(0, defense - self.attack)
        
        if vampirism:
            self.health += math.floor(max(0, self.attack - defense) * vampirism / 100)
        if max_health != None:
            if self.health > max_health:
                self.health = max_health

    def equip_weapon(self, weapon):
        self.health += weapon.health
        self.attack += weapon.attack
        if self.attack < 0:
            self.attack = 0
        try:
            self.defense += weapon.defense
            if self.defense < 0:
                self.defense = 0
        except:
            pass
        try:
            self.vampirism += weapon.vampirism
            if self.vampirism < 0:
                self.vampirism = 0
        except:
            pass
        try:
            self.max_health += weapon.health
        except:
            pass
        try:
            self.heal_power += weapon.heal_power
            if self.heal_power < 0:
                self.heal_power = 0
        except:
            pass

    @property
    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def show(self):
        try:
            vampirism = self.vampirism
        except:
            self.vampirism = 0
        try:
            defense = self.defense
        except:
            self.defense = 0
        try:
            heal_power = self.heal_power
        except:
            self.heal_power = 0
        
        print('health:', self.health, 'attack:', self.attack, \
              'defense:', self.defense, 'vampirism:', self.vampirism, 'heal_power:', self.heal_power)

class Knight(Warrior):
    def __init__(self):
        self.health = 50
        self.attack = 7

class Rookie(Warrior):
    def __init__(self):
        self.health = 50
        self.attack = 1

class Defender(Warrior):
    def __init__(self):
        self.health = 60
        self.attack = 3
        self.defense = 2

class Vampire(Warrior):
    def __init__(self):
        self.health = 40
        self.attack = 4
        self.vampirism = 50
        self.max_health = 40

class Lancer(Warrior):
    def __init__(self):
        self.health = 50
        self.attack = 6

    def spear_hit(self, enemy):
        defense = 0
        try:
            defense = enemy.defense
        except:
            pass
        enemy.health = enemy.health + min(0, defense - self.attack//2)

class Healer(Warrior):
    def __init__(self):
        self.health = 60
        self.attack = 0
        self.heal_power = 2
        
    def heal(self, unit):
        if isinstance(unit, (Warrior, Knight, Rookie, Lancer)):
            max_health = 50
        elif isinstance(unit, Vampire):
            max_health = 40
        else:
            max_health = 60
        
        unit.health += self.heal_power
        if unit.health > max_health:
             unit.health = max_health

class Warlord(Warrior):
    def __init__(self):
        self.health = 100
        self.attack = 4
        self.defense = 2

    def move_units(self, army):
        pass
        
        

'''
WEAPONS: Sword, Shield, GreatAxe, HellKatana, MagicWand
'''
class Weapon:
    def __init__(self, health, attack, defense, vampirism, heal_power):
        self.health = health
        self.attack = attack
        self.defense = defense
        self.vampirism = vampirism
        self.heal_power = heal_power

class Sword(Weapon):
    def __init__(self):
        self.health = 5
        self.attack = 2

class Shield(Weapon):
    def __init__(self):
        self.health = 20
        self.attack = -1
        self.defense = 2

class GreatAxe(Weapon):
    def __init__(self):
        self.health = -15
        self.attack = 5
        self.defense = -2
        self.vampirism = 10

class Katana(Weapon):
    def __init__(self):
        self.health = -20
        self.attack = 6
        self.defense = -5
        self.vampirism = 50

class MagicWand(Weapon):
    def __init__(self):
        self.health = 30
        self.attack = 3
        self.heal_power = 3

'''
1vs1 FIGHT FUNCTIONS
'''
def ffight(unit_1, unit_2, unit_3, unit_4):
    while unit_1.health > 0 and unit_3.health > 0:
        unit_1.hit(unit_3)
        if isinstance(unit_1, Lancer):
            unit_1.spear_hit(unit_4)
            print('lancer hits you')
        print('hp3:',unit_3.health)
        print('hp4:',unit_4.health)

        if isinstance(unit_2, Healer):
            unit_2.heal(unit_1)
            print('unit_1 was healed')

        if unit_3.health <= 0:
            break
        unit_3.hit(unit_1)
        if isinstance(unit_3, Lancer):
            unit_3.spear_hit(unit_2)
            print('lancer hits you')
        print('hp1:',unit_1.health)
        print('hp2:',unit_2.health)

        if isinstance(unit_4, Healer):
            unit_4.heal(unit_3)
            print('unit_3 was healed')

    if unit_1.health > 0:
        return True
    return False

def fight(unit_1, unit_2):
    turn = 1
    while unit_1.health > 0 and unit_2.health > 0:
        print('turn:', turn)
        unit_1.hit(unit_2)
        print('hp2:',unit_2.health)
        if unit_2.health <= 0:
            break
        unit_2.hit(unit_1)
        print('hp1:',unit_1.health)
        turn += 1
    if unit_1.health > 0:
        return True
    return False

'''
ARMY FIGHTS
'''
class Battle:
    def fight(self, army_1, army_2):
        while len(army_1.units) > 1 and len(army_2.units) > 1:
            result = ffight(army_1.units[0], army_1.units[1], army_2.units[0], army_2.units[1])
            if result:
                del army_2.units[0]
                print('army_2 lose the unit')
                army_2.sort_units()
                print('ARMY 2', army_2.units)
            else:
                del army_1.units[0]
                print('army_1 lose the unit')
                army_1.sort_units()
                print('ARMY 1', army_1.units)
        while len(army_1.units) > 0 and len(army_2.units) > 0:
            last = fight(army_1.units[0], army_2.units[0])
            if last:
                del army_2.units[0]
                print('army_2 lose the unit')
            else:
                del army_1.units[0]
                print('army_1 lose the unit')
        
        if len(army_1.units) > 0:
            return True
        return False

    def straight_fight(self, army_1, army_2):
        while len(army_1.units) > 0 and len(army_2.units) > 0:
            l1 = len(army_1.units)
            l2 = len(army_2.units)
            if l1 < l2:
                shortest = l1
            else:
                shortest = l2
            for i in range(shortest):
                x = fight(army_1.units[i], army_2.units[i])

            for i in range(len(army_1.units)):
                if army_1.units[i].health <= 0:
                    print(i, 'of 1 army are dead')
                    army_1.units[i] = 0
            for i in range(len(army_2.units)):
                if army_2.units[i].health <= 0:
                    print(i, 'of 2 army are dead')
                    army_2.units[i] = 0
            print(army_1.units, army_2.units)
            while 0 in army_1.units:
                army_1.units.remove(0)
            while 0 in army_2.units:
                army_2.units.remove(0)
            print(army_1.units, army_2.units)
        if len(army_1.units) > 0:
            return True
        return False
