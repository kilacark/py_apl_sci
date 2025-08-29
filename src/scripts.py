# %% # Python file with cells
## Import libraries
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib widget
# %% ## Computation
x = np.linspace(-2, 2, 100)
y = x**2
# %% ## Visualization
plt.figure()
plt.plot(x, y)
plt.show()
