import numpy as np
import csv

# CSV file
csv_file = './data.csv'

# Function to calculate the rate of change of a given dataset
def rate_change(table):
    """
    Rate change calc of CSV data

    Args:
        table (csv): data for calculations
    """
    # Read CSV data
    with open(table, 'r') as f:
        reader = csv.reader(f)
        next(f)  # Skip the header
        row_data = list(reader)

    # Unpack into numpy array
    data = [[float(t), float(x)] for t, x in row_data]
    np_data = np.array(data)

    # Delta T and X calculations
    delta_t = np_data[1:, 0] - np_data[:-1, 0]
    delta_x = np_data[1:, 1] - np_data[:-1, 1]

    # Calculate the rates of change
    rates = delta_t / delta_x
    return rates

# Use the rate_change function to calculate the rates
values = rate_change(csv_file)

# Output the calculated values and statistics
print(f'Rate change: {values}\n')
print(f'Lowers value: {np.amin(values)}')
print(f'Highest value: {np.amax(values)}')
print(f'Average value: {np.mean(values)}')
print(f'Standard deviation: {np.std(values)}')

# Output:
# The above prints the rate change, lowest value, highest value, average value, 
# and standard deviation of the rate of change calculated for the data.

# For linear regression, we'll calculate the slope (m) and y-intercept (c) for the best fit line
def linear_regression(table):
    """
    Performs linear regression on the provided CSV data to calculate the best-fit line's slope and intercept.
    """
    # Read CSV data
    with open(table, 'r') as f:
        reader = csv.reader(f)
        next(f)  # Skip the header
        row_data = list(reader)

    # Unpack into numpy arrays
    data = [[float(t), float(x)] for t, x in row_data]
    np_data = np.array(data)

    # Columns X and Y values
    X = np_data[:, 0]
    Y = np_data[:, 1]

    # N value (number of data points)
    n = len(X)

    # Two M line calc values (for slope calculation)
    m1 = (n * np.sum(X * Y)) - (np.sum(X) * np.sum(Y))
    m2 = (n * np.sum(X * X)) - (np.sum(X) * np.sum(X))
    m3 = m1 / m2  # Final slope calculation

    # Two C line calc values (for y-intercept calculation)
    c1 = (np.sum(Y) * np.sum(X * X)) - (np.sum(X) * np.sum(X * Y))
    c2 = (n * np.sum(X * X)) - (np.sum(X) * np.sum(X))
    c3 = c1 / c2  # Final y-intercept calculation

    return m3, c3

# Use linear_regression to calculate slope and y-intercept
values = linear_regression(csv_file)

# Print out the slope and intercept
print(values)

# Output:
# The above prints the slope (m) and y-intercept (c) for the linear regression.
# These coefficients describe the best fit line for the data.

