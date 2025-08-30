# %% # Python file with cells
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from core import core_funcs as cf

# %matplotlib widget  # noqa
# %% ## Computation
x = np.linspace(-2, 2, 100)
y = x**2
# %% ## Visualization
plt.figure()
plt.plot(x, y)
plt.show()
# %% ## pd.DataFrame
df = pd.DataFrame(data=[x, y], index=["x", "y"]).T
df
# %%
inp_l = [1, 2, 3]
cf.ext_list(inp_l, 10, 20)
# %%
