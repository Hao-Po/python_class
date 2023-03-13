def main():
    value = 2
    while(value % 2 == 0):
        value = int(input("Please enter odd number: "))
    for num in range(1, value + 1, 2):
        print(" " * int((value - num) / 2), "*" * num)
    for num in range(value - 2, 0, -2):
        print(" " * int((value - num) / 2), "*" * num)
