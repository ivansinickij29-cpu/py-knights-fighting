from app.knights.knight import Knight
from app.knights.weapon import Weapon
from app.knights.armour import Armour
from app.knights.potion import Potion


def prepare_knight(data: dict) -> Knight:
    knight = Knight(
        name=data["name"],
        power=data["power"],
        hp=data["hp"]
    )

    weapon_data = data["weapon"]
    weapon = Weapon(
        name=weapon_data["name"],
        power=weapon_data["power"]
    )
    knight.equip_weapon(weapon)

    for armour_data in data["armour"]:
        armour = Armour(
            name=armour_data["part"],
            protection=armour_data["protection"]
        )
        knight.equip_armour(armour)

    potion_data = data["potion"]
    if potion_data:
        potion = Potion(
            stat=potion_data["stat"],
            value=potion_data["value"]
        )
        knight.drink_potion(potion)

    return knight


def battle(knight1: dict, knight2: dict) -> str:
    k1 = prepare_knight(knight1)
    k2 = prepare_knight(knight2)

    while k1.hp > 0 and k2.hp > 0:
        damage_to_k2 = max(0, k1.power - k2.protection)
        k2.hp -= damage_to_k2
        if k2.hp <= 0:
            return k1.name

        damage_to_k1 = max(0, k2.power - k1.protection)
        k1.hp -= damage_to_k1
        if k1.hp <= 0:
            return k2.name

    return k1.name


KNIGHTS = {
    "lancelot": {
        "name": "Lancelot",
        "power": 35,
        "hp": 100,
        "armour": [],
        "weapon": {
            "name": "Metal Sword",
            "power": 50,
        },
        "potion": None,
    },
    "arthur": {
        "name": "Arthur",
        "power": 45,
        "hp": 75,
        "armour": [
            {
                "part": "helmet",
                "protection": 15,
            },
            {
                "part": "breastplate",
                "protection": 20,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Two-handed Sword",
            "power": 55,
        },
        "potion": None,
    },
    "mordred": {
        "name": "Mordred",
        "power": 30,
        "hp": 90,
        "armour": [
            {
                "part": "breastplate",
                "protection": 15,
            },
            {
                "part": "boots",
                "protection": 10,
            }
        ],
        "weapon": {
            "name": "Poisoned Sword",
            "power": 60,
        },
        "potion": {
            "name": "Berserk",
            "effect": {
                "power": +15,
                "hp": -5,
                "protection": +10,
            }
        }
    },
    "red_knight": {
        "name": "Red Knight",
        "power": 40,
        "hp": 70,
        "armour": [
            {
                "part": "breastplate",
                "protection": 25,
            }
        ],
        "weapon": {
            "name": "Sword",
            "power": 45
        },
        "potion": {
            "name": "Blessing",
            "effect": {
                "hp": +10,
                "power": +5,
            }
        }
    }
}
