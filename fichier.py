import random
import sys

def main():
    if len(sys.argv) != 2:
        exit(84);
    if sys.argv[1] == "ex1":
        ex1()
    if sys.argv[1] == "ex2":
        ex2()
    if sys.argv[1] == "ex3":
        i = ex3()
        print(i)
    if sys.argv[1] == "ex4":
        ex4()
    if sys.argv[1] == "ex5":
        ex5()
    if sys.argv[1] == "ex6":
        ex6()
    if sys.argv[1] == "ex7":
        ex7()
    if sys.argv[1] == "ex8":
        ex8()
    if sys.argv[1] == "ex9":
        ex9()

def ex1():
    for i in range(1, 101):
        if i % 3 == 0:
            print("Three", end="")
        if i % 5 == 0:
            print("Five", end="")
        if (i % 3 != 0 and i % 5 != 0):
            print(i, end="")
        print("")

def ex2():
    def calculate(args):
        added = False;
        sum = 0;
        if (type(args) != type([1, 2, 3])):
            return False
        for i in range(len(args)):
            if type(args[i]) == type("a"):
                try:
                    added = True
                    sum += int(args[i])
                except ValueError:
                    continue
        if added:
            return sum;
        return False;
    print(calculate(['4', '3', '-2']))
    print(calculate(453))
    print(calculate(['nothing', 3, '8', 2, '1']))
    print(calculate('54'))

def ex3():
    while True:
        return random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100])

def ex4():
    class Villager:
        def __init__(self, name, hp = 100, attack = 5, stamina = 100):
            self.hp = hp
            self.attack = attack
            self.stamina = stamina
            self.name = name
    boi = Villager("boi")
    print(boi.hp)
    print(boi.attack)
    print(boi.stamina)
    print(boi.name)

def ex5():
    class Villager:
        def __init__(self, name, hp = 100, attack = 5, stamina = 100):
            self.hp = hp
            self.attack = attack
            self.stamina = stamina
            self.name = name
        def fattack(self):
            if self.stamina >= 10:
                self.stamina -= 10;
        def rest(self):
            self.stamina = 100
        def damage(self, damage):
            self.hp -= damage
            if self.hp <= 0:
                print("I'm dead aled pitier je mor")
        def speak(self):
            print("Hello my name is "+self.name+"!")
    boi = Villager("boi")
    print(boi.stamina)
    boi.fattack()
    print(boi.stamina)
    boi.rest()
    print(boi.stamina)
    boi.damage(10)
    print(boi.hp)
    boi.damage(100)
    boi.speak()

def ex6():
    class Villager:
        def __init__(self, name, hp = 100, attack = 5, stamina = 100):
            self.hp = hp
            self.attack = attack
            self.stamina = stamina
            self.name = name
        def fattack(self):
            if self.stamina >= 10:
                self.stamina -= 10;
        def rest(self):
            self.stamina = 100
        def damage(self, damage):
            self.hp -= damage
            if self.hp <= 0:
                print("I'm dead aled pitier je mor")
        def speak(self):
            print("Hello my name is "+self.name+"!")
    class Knight(Villager):
        def __init__(self, name, hp = 150, attack = 15, stamina = 100, armor = 50):
            self.hp = hp
            self.attack = attack
            self.stamina = stamina
            self.name = name
            self.armor = armor
        def special(self):
            self.stamina -= 50

    boi = Knight("boi")
    print(boi.stamina)
    boi.fattack()
    print(boi.stamina)
    boi.rest()
    print(boi.stamina)
    boi.damage(10)
    print(boi.hp)
    boi.damage(100)
    boi.special()

def ex7():

if __name__ == "__main__":
    main()