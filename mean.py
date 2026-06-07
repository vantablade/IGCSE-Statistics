import math

mean_type = input('Enter the type of mean you want to calculate (arithmetic, geometric, weighted): ')
numbers = []

while True:
        value = input('Add a number to the list (or done to finish): ')
        if value.lower == 'done':
            break
        try:
            numbers.append(float(value))
        except ValueError:
            print('Please print a valid number')

if mean_type.lower() == 'arithmetic':
    mean = sum(numbers) / len(numbers)
elif mean_type.lower() == 'geometric':
    mean = math.prod(numbers) ** (1 / len(numbers))
elif mean_type.lower() == 'weighted':
    weights = []
    for i in numbers:
         weight = input(f'Enter the weight of value: {numbers[i]}: ')
         weights.append(weight)
    total = sum(weights)
    weighted_prod = math.prod(x ** w for x, w in zip(numbers, weights))
    mean = weighted_prod ** (1 / total)

print(f'The {mean_type} mean is {mean}')