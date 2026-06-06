import matplotlib.pyplot as plt
import statistics

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

q1, median, q3 = statistics.quantiles(numbers, n=4)
print(f"Lower Quartile (Q1): {q1}")
print(f"Median (Q2): {median}")
print(f"Upper Quartile (Q3): {q3}")

interquartile_range = q3 - q1
print(f"Interquartiles Range: {interquartile_range}")

small_outlier = q1 - 1.5 * interquartile_range
large_outlier = q3 + 1.5 * interquartile_range
print(f'Anything <{small_outlier} or >{large_outlier} is an outlier')

for n in numbers:
    if n < small_outlier or large_outlier:
        outliers.append(n)

if len(outliers) > 0:
    print(f'Outliers: {outliers}')
else:
    print('There are no outliers')

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

