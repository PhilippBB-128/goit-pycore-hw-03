import random
def get_numbers_ticket(min: int, max: int, quantity: int):
    if not (1 <= min <= max <= 1000):
        print("Помилка")
        return []
    lottery_numbers = random.sample(range(min, max), quantity)
    lottery_numbers.sort()
    return lottery_numbers
    
   
lottery_number = get_numbers_ticket(1, 1000, 5)
print("Ваші лотерейні числа:", lottery_number)
 
 
 