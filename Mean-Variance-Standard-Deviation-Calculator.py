import statistics

def advanced_stats(numbers):
    if not numbers:
        return "Error: List is empty"

    mean_val = sum(numbers) / len(numbers)
    variance_val = sum((x - mean_val)**2 for x in numbers) / len(numbers)
    std_val = variance_val ** 0.5

    median_val = statistics.median(numbers)

    try:
        mode_val = statistics.mode(numbers)
    except:
        mode_val = "No unique mode"

    minimum = min(numbers)
    maximum = max(numbers)
    data_range = maximum - minimum

    q1 = statistics.quantiles(numbers, n=4)[0]
    q3 = statistics.quantiles(numbers, n=4)[2]
    iqr = q3 - q1

    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = [x for x in numbers if x < lower_bound or x > upper_bound]

    minmax_norm = [(x - minimum) / data_range for x in numbers]
    zscore_norm = [(x - mean_val) / std_val for x in numbers]

    return {
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
        "Min-Max Normalized": [round(x, 4) for x in minmax_norm],
        "Z-Score Normalized": [round(x, 4) for x in zscore_norm],
    }

user_input = input("Enter numbers separated by commas: ")

try:
    data = [float(x.strip()) for x in user_input.split(",")]
    result = advanced_stats(data)

    print("\n--- RESULTS ---")
    for k, v in result.items():
        print(f"{k}: {v}")

except ValueError:
    print("Error: Please enter only numbers separated by commas.")
