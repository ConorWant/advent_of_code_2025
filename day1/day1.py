def move_wheel(direction, distance, current_number):
    max_number = 99
    min_number = 0

    if direction == "R":
        next_number = current_number + distance

        if next_number > max_number:
            next_number = (current_number + distance) % 100

        return next_number


    if direction == "L":
        next_number = current_number - distance

        if next_number < min_number:
            next_number = (current_number - distance) % 100

        return next_number


count = 0
with open("puzzle_input.txt", "r") as file:
    lines = file.readlines()
start_number = 50
for line in lines:
    direction = line[0]
    distance = int(line[1:-1])

    new_number = move_wheel(direction, distance, start_number)
    start_number = new_number
    if new_number == 0:
        count += 1



print(count)