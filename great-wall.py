import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


X = pd.read_csv('data/great-wall.csv').values


with plt.style.context('dark_background'):
    fig, ax = plt.subplots(figsize=(16, 9), dpi=300)
    d, x = X.T
    ax.scatter(x, d, s=0.75, linewidth=0, color=plt.cm.magma(1.0))
    ax.set_xlabel('y position (Mpc)')
    ax.set_ylabel('Distance from Earth (Mpc)')
    ax.set_xlim(np.min(x), np.max(x))
    ax.set_ylim(np.min(d), np.max(d))
    ax.set_aspect('equal')
    fig.savefig('_images/great-wall.png')

