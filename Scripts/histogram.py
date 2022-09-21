import pandas as pd
import sys

filename = sys.argv[2]
df=pd.read_csv(filename)
df

import matplotlib.pyplot as plt
hist = df['column'].hist(bins=100)