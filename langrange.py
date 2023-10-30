import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


def lagrange_interpolation(x, y):
    lagrange_func = interp1d(x, y, kind='quadratic')
    return lagrange_func


# Generate data points
x = np.linspace(0, 10, 11)
y = np.sin(x)
# Plot original data
plt.scatter(x, y, color='red', label='original Data')

# Generate interpolation data
lagrange_func = lagrange_interpolation(x, y)
x_interp = np.linspace(0, 10, 101)
y_interp = lagrange_func(x_interp)
# Plot interpolated data
plt.plot(x_interp, y_interp, color='blue', label='Interpolated Data')
plt.legend()
# Display the plot
plt.show()
