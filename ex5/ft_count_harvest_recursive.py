def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))
    i = 1

    def recusive(i, day):
        if i > day:
            return
        print(f"Day {i}")
        recusive(i + 1, day)
    recusive(i, day)
    print("Harvest time!")
