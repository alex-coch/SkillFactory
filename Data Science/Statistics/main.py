
from scipy.stats import norm
import math

def confidence_interval_norm(alpha, sigma, n, mean):
    value = -norm.ppf(alpha / 2) * sigma / math.sqrt(n)
    return mean - value, mean + value

from scipy.stats import t

def confidence_interval_t(alpha, s, n, mean):
    value = -t.ppf(alpha / 2, n - 1) * s / math.sqrt(n)
    return mean - value, mean + value

print(confidence_interval_norm(0.01, 1150, 250, 3540))