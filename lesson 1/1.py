class Warrior:
    health: int
    attack: int

    def __init__(self):
        self.health = 50
        self.attack = 5

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False


class Knight(Warrior):

    def __init__(self):
        super().__init__()
        self.attack = 7


def fight(w, k):
    while True:
        if w.is_alive():
            k.health -= w.attack
        else:
            return False
        if k.is_alive():
            w.health -= k.attack
        else:
            return True

class Army:

    def __init__(self):
        self.army = []

    def add_units(self, who, count):
        for i in range(count):
            self.army.append(who())


w1 = Warrior()
k1 = Knight()
print(fight(w1, k1))
a1 = Army()
print(a1.add_units(Warrior, 20))
print(a1.army)