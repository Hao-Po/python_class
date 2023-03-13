def main():
    value = int(input("Please enter a value: "))
    for num in range(value):
        print("#{}#".format(" " * num))
