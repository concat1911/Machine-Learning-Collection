import numpy as np
import pandas as pd
import missingno as msno
import seaborn as sn
import matplotlib.pyplot as plt

# Data import
data = pd.read_csv("../data/steam/steam.csv")
data.columns

# Missing data checking
msno.matrix(data, figsize=(10, 3))

# Distribution
fig, axes = plt.subplots(nrows=2, ncols=1)
fig.set_size_inches(10, 20)
sn.boxplot(data=data, orient="v", ax=axes[0])

# COrrelation analasys
corrMatt = data.corr()
mask = np.array(corrMatt)
mask[np.tril_indices_from(mask)] = False
fig, ax = plt.subplots()
fig.set_size_inches(20, 10)
sn.heatmap(corrMatt, mask=mask, vmax=.8, square=True, annot=True)