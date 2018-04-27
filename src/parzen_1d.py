# ========================================
# [] File Name : parzen_1d.py
#
# [] Creation Date : April 2018
#
# [] Author 2 : Ali Gholami
# ========================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from sklearn.neighbors import KernelDensity

# Seed the random number generator
np.random.seed(1)
NUM_SAMPLES = 100
NUM_BINS = 20
RANGE_LOW = 1
RANGE_HIGH = 20
BANDWIDTH = 0.1

# Density characteristics
modal1_mean = 5
modal2_mean = 15
modal1_variance = 1
modal2_variance = 1

# Generate some samples from the given multi modal distribution
sample_set = np.concatenate((np.random.normal(modal1_mean, modal1_variance, int(0.3 * NUM_SAMPLES)),
                            np.random.normal(modal2_mean, modal2_variance, int(0.7 * NUM_SAMPLES))))[:, np.newaxis]

x_plot = np.linspace(RANGE_LOW, RANGE_HIGH, 1000)[:, np.newaxis]
print(x_plot.shape)
bins = np.linspace(RANGE_LOW, RANGE_HIGH, NUM_BINS)

true_dens = (0.3 * norm(modal1_mean, modal1_variance).pdf(x_plot[:, 0])
             + 0.7 * norm(modal2_mean, modal2_variance).pdf(x_plot[:, 0]))
plt.fill(x_plot[:, 0], true_dens, fc='black', alpha=0.2,
        label='Input Distribution')

# Fit Gaussian windows on the samples
kde = KernelDensity(kernel='gaussian', bandwidth=BANDWIDTH).fit(sample_set)
log_dens = kde.score_samples(x_plot)
plt.fill(x_plot[:, 0], np.exp(log_dens), fc='darkblue', label='Gaussian Windows Estimation')
plt.legend(loc='upper left')
plt.show()

