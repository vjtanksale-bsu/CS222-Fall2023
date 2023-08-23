def main():
    i = 0
    j = 0
    while i < 4:
        print(f"Outer loop {i}")
        i += 1
        while j < 3:
            print(f"Inner loop {j}")
            j += 1


main()
