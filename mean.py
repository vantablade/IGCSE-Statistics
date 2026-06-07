import math

mean_type = input('Enter the type of mean you want to calculate (arithmetic, geometric, weighted): ').strip().lower()

numbers = []
while True:
    value = input('Add a number to the list (or done to finish): ')
    if value.strip().lower() == 'done':
        break
    try:
        numbers.append(float(value))
    except ValueError:
        print('Please type a valid number')

if not numbers:
    print("No numbers were entered.")
else:
    if mean_type == 'arithmetic':
        mean = sum(numbers) / len(numbers)
        print(f'The {mean_type} mean is {mean:.4f}')
        
    elif mean_type == 'geometric':
        mean = math.prod(numbers) ** (1 / len(numbers))
        print(f'The {mean_type} mean is {mean:.4f}')
        
    elif mean_type == 'weighted':
        weights = []
        for num in numbers:
            weight = float(input(f'Enter the weight for value {num}: '))
            weights.append(weight)
            
        total_weights = sum(weights)
        # Multiply each number by its weight, then take the (1 / total_weights) root
        weighted_prod = math.prod(x ** w for x, w in zip(numbers, weights))
        mean = weighted_prod ** (1 / total_weights)
        print(f'The {mean_type} mean is {mean:.4f}')
        
    else:
        print('Invalid mean type selected.')
