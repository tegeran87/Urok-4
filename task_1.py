cfrom functools import reduce

def mean(values):
    return sum(values) / len(values)

def pearson_correlation(x, y):
    n = len(x)

    mean_x = mean(x)
    mean_y = mean(y)

    covariance = sum(map(lambda xi, yi: (xi - mean_x) * (yi - mean_y), x, y))
    std_dev_x = (reduce(lambda acc, xi: acc + (xi - mean_x)**2, x, 0) / n)**0.5
    std_dev_y = (reduce(lambda acc, yi: acc + (yi - mean_y)**2, y, 0) / n)**0.5

    correlation = covariance / (std_dev_x * std_dev_y)

    return correlation

# Пример использования
array1 = [1, 2, 3, 4, 5]
array2 = [5, 4, 3, 2, 1]

correlation = pearson_correlation(array1, array2)
print(f"Корреляция Пирсона между массивами: {correlation}")