# ========================================
# [] File Name : parzen_2d.py
#
# [] Creation Date : April 2018
#
# [] Author 2 : Ali Gholami
# ========================================

import numpy as np
import matplotlib.pyplot as pl
import scipy.stats as st

# Seed the random number generator
np.random.seed(1)
NUM_SAMPLES = 500
NUM_BINS = 20
RANGE_LOW = 1
RANGE_HIGH = 20
BANDWIDTH = 1

# Density characteristics
MEAN = [10, 10]
COV = [[5, 0], [0, 5]]


sample_set = np.random.multivariate_normal(MEAN, COV, NUM_SAMPLES)
x = sample_set[:, 0]
y = sample_set[:, 1]

# Peform the kernel density estimate
xx, yy = np.mgrid[RANGE_LOW:RANGE_HIGH:100j, RANGE_LOW:RANGE_HIGH:100j]
positions = np.vstack([xx.ravel(), yy.ravel()])
values = np.vstack([x, y])
kernel = st.gaussian_kde(values)
f = np.reshape(kernel(positions).T, xx.shape)

fig = pl.figure()
ax = fig.gca()
ax.set_xlim(RANGE_LOW, RANGE_HIGH)
ax.set_ylim(RANGE_LOW, RANGE_HIGH)

# Actual Density Area
cfset = ax.contourf(xx, yy, f, cmap='Blues', label='Input Distribution')

# Contour plots of Estimated
cset = ax.contour(xx, yy, f, colors='k', label='Gaussian Windows Estimation')

# Label plot
ax.clabel(cset, inline=1, fontsize=10)

ax.set_xlabel('Y1')
ax.set_ylabel('Y0')

pl.show()