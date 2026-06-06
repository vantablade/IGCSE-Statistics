import matplotlib.pyplot as plt

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

if len(numbers) == 0:
    print('No data entered')
    exit()
elif len(numbers) < 2:
    print('At least two values are required.')
    exit()

q1_index = 0.25 * (len(numbers) + 1)
median_index = 0.5 * (len(numbers) + 1)
q3_index = 0.75 * (len(numbers) + 1)

print(q1_index, median_index, q3_index)

plt.boxplot(
    numbers,
    vert = False,
    whis = 1.5,
    flierprops=dict(marker='x', markersize=8),
)

plt.title("Box Plot of Data")
plt.xlabel("Values")
plt.grid(True, which='both', linestyle='--', alpha=0.5)

plt.show()

