import matplotlib.pyplot as plt
from Main import main
import numpy as np

sims = 1000

result = []

for i in range(0, sims):
    result.append(main())


# non logged data
plt.hist(result, bins=20)
plt.show()

# logged data
resultln = np.log(result)
plt.hist(resultln, bins=20)
plt.show()
