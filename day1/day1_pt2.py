def move_wheel(direction, distance, current_number):
    max_number = 99
    min_number = 0
    zero_counter = 0

    if direction == "R":
        for n in range(distance):
            current_number = (current_number + 1) % 100
            if current_number == 0:
                zero_counter += 1

        return current_number, zero_counter


    if direction == "L":
        for n in range(distance):
            current_number = (current_number - 1) % 100
            if current_number == 0:
                zero_counter += 1
        return current_number, zero_counter

count = 0

with open("puzzle_input.txt", "r") as file:
    lines = file.readlines()
start_number = 50
for line in lines:
    direction = line[0]
    distance = int(line[1:-1])

    new_number, zeros = move_wheel(direction, distance, start_number)
    start_number = new_number

    count += zeros


print(count)