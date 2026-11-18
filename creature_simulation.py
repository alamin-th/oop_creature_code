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


class SwimmingCreature(Creature):
    def __init__(self, name, hp, attack_power, depth=0):
        Creature.__init__(self, name, hp, attack_power)
        self._depth = depth

    @property
    def depth(self):
        return self._depth

    def dive_to(self, new_depth):
        self._depth = new_depth
        print(f"{self.name} dives to depth {self.depth}!")

    def attack(self, target):
        print(f"{self.name} surges from depth {self.depth} and strikes {target.name} for {self.attack_power} damage!")
        target.hp -= self.attack_power

    def __str__(self):
        return f"{self.name}: HP={self.hp}, ATK={self.attack_power}, DEPTH={self.depth}"


class FireCreature(Creature):
    def __init__(self, name, hp, attack_power, fire_level=0):
        Creature.__init__(self, name, hp, attack_power)
        self._fire_level = fire_level

    @property
    def fire_level(self):
        return self._fire_level

    def emit_fire(self, new_fire_level):
        self._fire_level = max(0, min(100, new_fire_level))
        print(f"{self.name} raises fire level to {self.fire_level}!")

    def attack(self, target):
        bonus = self.fire_level // 10
        total_damage = self.attack_power + bonus
        print(f"{self.name} unleashes a blazing attack (fire level {self.fire_level}) on {target.name} for {total_damage} damage!")
        target.hp -= total_damage

    def __str__(self):
        return f"{self.name}: HP={self.hp}, ATK={self.attack_power}, FIRE={self.fire_level}"


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

    print("\n---- swimming creature tests ----")
    s1 = SwimmingCreature("Kraken", 60, 12)
    print(s1)
    s1.dive_to(50)
    s1.attack(c2)
    print(c2)

    print("\n---- fire creature tests ----")
    fc1 = FireCreature("Phoenix", 45, 7)
    print(fc1)
    fc1.emit_fire(80)
    fc1.attack(c2)
    print(c2)
    print("Phoenix alive?", fc1.is_alive())