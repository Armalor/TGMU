# Словари.

character = {
    'hp': 100,
    'mana': 50,
    'ammo': {
        'left_hand': 'shield',
        'right_hand': 'sword',
    }
}

print(f'У персонажа {character["hp"]} здоровья и {character["mana"]} маны')

character['mana'] -= 20

print(f'У персонажа {character["hp"]} здоровья и {character["mana"]} маны')

print(f'Оружие. В правой руке {character["ammo"]["right_hand"]}')
print(f'Оружие. В лувой руке {character["ammo"]["left_hand"]}')