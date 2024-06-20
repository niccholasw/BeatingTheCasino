import matplotlib.pyplot as plt
from Main import main
import numpy as np

sims = 10000
result = []

for i in range(0, sims):
    result.append(main())

fig, axs = plt.subplots(2)
fig.suptitle('Non-Logged vs Logged distribution')
axs[0].hist(result, bins=50)
axs[1].hist(np.log(result), bins=50)

plt.show()