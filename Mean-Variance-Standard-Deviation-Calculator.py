import statistics
from collections import Counter
import math


def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


def calculate_variance(numbers, mean):
    return sum((x - mean) ** 2 for x in numbers) / len(numbers)


def calculate_std(variance):
    return variance ** 0.5


def bubble_sort(arr):
    arr = arr[:]
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def moving_average(data, window=3):
    result = []

    if len(data) < window:
        return result

    for i in range(len(data) - window + 1):
        avg = sum(data[i:i + window]) / window
        result.append(round(avg, 4))

    return result


def is_prime(n):
    if n < 2 or n != int(n):
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True


def display_histogram(numbers):
    print("\n--- HISTOGRAM ---")
    for num in numbers:
        if num > 0 and num == int(num):
            print(f"{int(num)}: {'*' * int(num)}")


def advanced_stats(numbers):
    if not numbers:
        return "Error: List is empty"

    count = len(numbers)
    total_sum = sum(numbers)

    mean_val = calculate_mean(numbers)
    variance_val = calculate_variance(numbers, mean_val)
    std_val = calculate_std(variance_val)

    median_val = statistics.median(numbers)

    try:
        mode_val = statistics.mode(numbers)
    except:
        mode_val = "No unique mode"

    minimum = min(numbers)
    maximum = max(numbers)
    data_range = maximum - minimum

    sorted_numbers = bubble_sort(numbers)

    q1 = statistics.quantiles(numbers, n=4)[0]
    q3 = statistics.quantiles(numbers, n=4)[2]
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr

    outliers = [x for x in numbers if x < lower_bound or x > upper_bound]

    if data_range != 0:
        minmax_norm = [(x - minimum) / data_range for x in numbers]
    else:
        minmax_norm = [0 for _ in numbers]

    if std_val != 0:
        zscore_norm = [(x - mean_val) / std_val for x in numbers]
    else:
        zscore_norm = [0 for _ in numbers]

    frequency = dict(Counter(numbers))

    positive_nums = [x for x in numbers if x > 0]

    if len(positive_nums) == len(numbers):
        geometric_mean = statistics.geometric_mean(numbers)
    else:
        geometric_mean = "Not possible"

    try:
        harmonic_mean = statistics.harmonic_mean(numbers)
    except:
        harmonic_mean = "Not possible"

    cv = (std_val / mean_val) * 100 if mean_val != 0 else 0

    percentile_10 = sorted_numbers[int(0.1 * (count - 1))]
    percentile_90 = sorted_numbers[int(0.9 * (count - 1))]

    if mean_val > median_val:
        skewness = "Right Skewed"
    elif mean_val < median_val:
        skewness = "Left Skewed"
    else:
        skewness = "Symmetric"

    even_count = len([x for x in numbers if x % 2 == 0])
    odd_count = len([x for x in numbers if x % 2 != 0])

    positive = len([x for x in numbers if x > 0])
    negative = len([x for x in numbers if x < 0])
    zeros = len([x for x in numbers if x == 0])

    prime_numbers = [x for x in numbers if is_prime(x)]

    reversed_data = list(reversed(numbers))
    unique_values = list(set(numbers))
    moving_avg = moving_average(numbers)

    return {
        "Count": count,
        "Sum": round(total_sum, 4),
        "Mean": round(mean_val, 4),
        "Variance": round(variance_val, 4),
        "Standard Deviation": round(std_val, 4),
        "Median": median_val,
        "Mode": mode_val,
        "Min": minimum,
        "Max": maximum,
        "Range": data_range,
        "Q1": round(q1, 4),
        "Q3": round(q3, 4),
        "IQR": round(iqr, 4),
        "Outliers": outliers,
        "Geometric Mean": geometric_mean,
        "Harmonic Mean": harmonic_mean,
        "Coefficient of Variation (%)": round(cv, 4),
        "10th Percentile": percentile_10,
        "90th Percentile": percentile_90,
        "Skewness": skewness,
        "Frequency Distribution": frequency,
        "Sorted Data": sorted_numbers,
        "Reversed Data": reversed_data,
        "Unique Values": unique_values,
        "Even Count": even_count,
        "Odd Count": odd_count,
        "Positive Count": positive,
        "Negative Count": negative,
        "Zero Count": zeros,
        "Prime Numbers": prime_numbers,
        "Moving Average": moving_avg,
        "Min-Max Normalized": [round(x, 4) for x in minmax_norm],
        "Z-Score Normalized": [round(x, 4) for x in zscore_norm],
    }


def save_report(result):
    with open("stats_report.txt", "w") as file:
        for key, value in result.items():
            file.write(f"{key}: {value}\n")
    print("Report saved to stats_report.txt")


def menu():
    print("\n========== STATISTICS ANALYZER ==========")
    print("1. Analyze Data")
    print("2. Exit")


while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        user_input = input("Enter numbers separated by commas: ")

        try:
            data = [float(x.strip()) for x in user_input.split(",")]
            result = advanced_stats(data)

            print("\n--- RESULTS ---")
            for k, v in result.items():
                print(f"{k}: {v}")

            display_histogram(data)

            save = input("\nSave report? (yes/no): ").lower()
            if save == "yes":
                save_report(result)

        except ValueError:
            print("Error: Please enter only numbers.")

    elif choice == "2":
        print("Program closed.")
        break

    else:
        print("Invalid choice.")
