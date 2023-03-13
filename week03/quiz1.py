def main():
    value = int(input("Please enter a value: "))
    for num in range(value, 0, -1):
        print("*" * num)
    for num in range(2, value + 1):
        print("*" * num)
