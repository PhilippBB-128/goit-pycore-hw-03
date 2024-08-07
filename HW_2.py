import random
def get_numbers_ticket(min: int, max: int, quantity: int):
    lottery_number = []
    while len(lottery_number) < quantity:
        numbers = random.randint(1, 1000)
        if numbers not in lottery_number:
            lottery_number.append(numbers)
    return sorted(lottery_number)
    
   
lottery_number = get_numbers_ticket(1, 1000, 5)
print("Ваші лотерейні числа:", lottery_number)
 
 
 