import pandas as pd
import numpy as np

ser = pd.Series(np.random.randint(1, 100, 10))

print("Pandas Series with 10 random numbers:")
print(ser)