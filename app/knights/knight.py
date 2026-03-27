class Knight:
    def __init__(self, name: str, power: int, hp: int) -> None:
        self.name = name
        self.power = power
        self.hp = hp
        self.protection = 0

    def equip_weapon(self, weapon) -> None:
        self.power += weapon.power

    def equip_armour(self, armour) -> None:
        self.protection += armour.protection

    def drink_potion(self, potion) -> None:
        if potion.stat == "power":
            self.power += potion.value
        elif potion.stat == "hp":
            self.hp += potion.value
        elif potion.stat == "protection":
            self.protection += potion.value
