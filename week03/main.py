import quiz1, quiz2, quiz3, quiz4, quiz5

def main():
    keep_going = "y"
    while keep_going == "y":
        print("1. Print double triangle")
        print("2. Print spacing triangle")
        print("3. Print diamond")
        print("4. Print grid")
        print("5. Guessing game")
        select_game = str(input("Please select game: "))
        if 1 <= int(select_game) <= 5:
            switch = {"1" : quiz1, "2" : quiz2, "3" : quiz3, "4" : quiz4, "5" : quiz5}
            switch[select_game].main()
            keep_going = input("Test again (y/n)? ")

if __name__ == '__main__':
    main()