import math
numbers = []
outliers = []

while True:
    value = input("Add a number to the list (or 'done' to finish): ")
    if value.lower() == 'done':
        break

    try:
        numbers.append(float(value))
    except ValueError:
        print('Please print a valid number')

population_size = len(numbers)

if len(numbers) == 0:
    print('No data entered')
    exit()
elif len(numbers) < 2:
    print('At least two values are required.')
    exit()

mean = sum(numbers) / population_size
print(f'Mean = {mean:.2f}')
top_half_total = 0

for n in numbers:
    top_half_total += ((n - mean)**2)

standard_deviation = math.sqrt(top_half_total / population_size)
print(f'Standard deviation = {standard_deviation:.2f}')

for n in numbers:
    if n >= 3 * standard_deviation + mean:
        outliers.append(n)

if len(outliers) > 0:     
    print(f'The outliers are: {outliers}')
else:
    print('There are no outliers.')