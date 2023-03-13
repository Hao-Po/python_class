import random

def main():
    start = 0; end = 100
    answer = random.randint(start, end)
    guessing(answer, start, end)

def guessing(answer, start, end):   
    achieve_limit = 0
    while True:
        guess_number = int(input(f"Please guess a number from {start:>2d} to {end:>3d}: "))
        if guess_number == answer:
            print("You passed")
            return
        if start <= guess_number <= end:
            if guess_number > answer:
                end = guess_number
            if guess_number < answer:
                start = guess_number
        achieve_limit += 1
        if achieve_limit > 9:
            print("Achieve Limitted")
            return