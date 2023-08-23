def main():
    numbers = [7, 5, 19, 3]
    i = 0
    while i < len(numbers):
        print(numbers[i])
        i += 1

    print()

    total = 0
    j = 0
    while j < len(numbers):
        total += numbers[j]
        j += 1
    print(total)


main()
