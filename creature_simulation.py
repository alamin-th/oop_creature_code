class Creature:
    def __init__(self, name, hp, attack_power):
        self._name = name
        self._hp = hp
        self._attack_power = attack_power

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @property
    def attack_power(self):
        return self._attack_power

    @hp.setter
    def hp(self, new_hp):
        self._hp = new_hp

    def attack(self, target):
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage!")
        target.hp -= self.attack_power

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: HP={self.hp}, ATK={self.attack_power}"


class FlyingCreature(Creature):
    def __init__(self, name, hp, attack_power, altitude=0):
        Creature.__init__(self, name, hp, attack_power)
        self._altitude = altitude

    @property
    def altitude(self):
        return self._altitude

    def fly_to(self, new_altitude):
        self._altitude = new_altitude
        print(f"{self.name} flies to altitude {self.altitude}!")

    def attack(self, target):
        print(f"{self.name} dives from altitude {self.altitude} and strikes {target.name} for {self.attack_power} damage!")
        target.hp -= self.attack_power

    def __str__(self):
        return f"{self.name}: HP={self.hp}, ATK={self.attack_power}, ALT={self.altitude}"


if __name__ == "__main__":
    print("\n---- creature tests ----")
    c1 = Creature("Goblin", 30, 5)
    c2 = Creature("Orc", 40, 8)
    print(c1)
    print(c2)
    c1.attack(c2)
    print(c2)
    print("c2 alive?", c2.is_alive())

    print("\n---- flying creature tests ----")
    f1 = FlyingCreature("Dragon", 50, 10)
    print(f1)
    f1.fly_to(100)
    f1.attack(c2)
    print(c2)