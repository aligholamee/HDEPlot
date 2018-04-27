# ========================================
# [] File Name : parzen_2d.py
#
# [] Creation Date : April 2018
#
# [] Author 2 : Ali Gholami
# ========================================

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.neighbors import KernelDensity

# Seed the random number generator
np.random.seed(1)
NUM_SAMPLES = 800
NUM_BINS = 20
RANGE_LOW = 1
RANGE_HIGH = 20
BANDWIDTH = 0.2

# Density characteristics
MEAN = [10, 10]
COV = [[5, 0], [0, 5]]


def kde2D(x, y, bandwidth, xbins=100j, ybins=100j, **kwargs): 
    """Build 2D kernel density estimate (KDE)."""

    # create grid of sample locations (default: 100x100)
    xx, yy = np.mgrid[x.min():x.max():xbins, 
                      y.min():y.max():ybins]

    xy_sample = np.vstack([yy.ravel(), xx.ravel()]).T
    xy_train  = np.vstack([y, x]).T

    kde_skl = KernelDensity(bandwidth=bandwidth, **kwargs)
    kde_skl.fit(xy_train)

    # score_samples() returns the log-likelihood of the samples
    z = np.exp(kde_skl.score_samples(xy_sample))
    return xx, yy, np.reshape(z, xx.shape)


sample_set = np.random.multivariate_normal(MEAN, COV, NUM_SAMPLES)

xx, yy, zz = kde2D(sample_set[:, 0], sample_set[:, 1], BANDWIDTH)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Actual Density Area
ax.plot_surface(xx, yy, zz, facecolor='white')

plt.show()