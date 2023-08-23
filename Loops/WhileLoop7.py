def main():
    while True:
        number = input("Enter a number between 1-10 or no to quit")
        if number == "no":
            break
        else:
            for i in range(0, int(number)):
                print("Hello")


main()
