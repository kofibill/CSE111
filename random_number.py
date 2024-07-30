import random

def main():
    numbers_list=[16.2, 75.1, 52.3]
    print(numbers_list)
    append_random_numbers(numbers_list)
    print(numbers_list)
    append_random_numbers(numbers_list, 3)
    print(numbers_list)

def append_random_numbers(numbers_list, quantity=1):
    for _ in range(0, quantity):
        ran_number=round(random.uniform(0, 100), 1)
        numbers_list.append(ran_number)

main()
