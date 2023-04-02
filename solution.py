import pandas as pd
import numpy as np

from scipy.stats import norm

chat_id = 1109095907


def solution(p: float, x: np.array) -> tuple:
    x_n = x.max()
    left = 0.071 + x_n / 2
    right = 0.071 + x_n / (1 + (1 - p) ** (1 / x.shape[0]))
    return left, right

