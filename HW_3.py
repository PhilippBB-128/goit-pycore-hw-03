import re

def normalize_phone(phone_number):
    sanitar_number = re.sub("[^0-9]", "", phone_number)
    if not sanitar_number.startswith('38'):
        sanitar_number = '+38' + sanitar_number
    else:
        sanitar_number = '+' + sanitar_number
    return sanitar_number
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32++++34",
    "     05034512",
    "(050)8889900",
    "38050-111-22-2",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


