import matplotlib.pyplot as plt
from Main import main

sims = 1000

result = []

for i in range(0, sims):
    result.append(main())

plt.hist(result)