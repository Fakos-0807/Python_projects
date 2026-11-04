import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("StudentsPerformance.csv")
df.plot(x = 'reading score', y = 'writing score', kind='scatter')
plt.show()





