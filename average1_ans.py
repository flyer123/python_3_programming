# initialise variables
count, sum, lowest, highest = 0, 0, 0, 0
numbers = []

# Enter the numbers in a cicle
while True:
    try:
        s = input("Enter a number, ^Z to stop: ")
        if s == '^Z':
            break
        i = int(s)
        sum += i
        count += 1
        if count == 1:
            lowest = i
            highest = i
        else:
            if i < lowest:
                lowest = i
            if i > highest:
                highest = i
        numbers.append(i)
    except ValueError as err:
        print(err)

# Print the outputs
print("numbers = ", numbers)
print('count = ', count, 'sum = ', sum, 'lowest = ', lowest, 'highest = ', highest, 'mean = ', sum / count)

