def read_input_file(dayNumber: int, livemode: bool):
    if (livemode):
        path = f'./data/day{dayNumber:02}/input'
    else:
        path = f'./data/day{dayNumber:02}/input_test'

    try:
        with open(path, 'r') as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"The file {path} was not found.")
        raise
    except IOError:
        print("An error occurred while reading the file.")
        raise
