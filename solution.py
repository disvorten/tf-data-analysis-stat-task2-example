import pandas as pd
import numpy as np

chat_id = 1109095907


def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    x_n = x.max()
    loc = 0.071
    left = x_n
    right = loc + (x_n - loc) / (alpha ** (1 / x.shape[0]))
    return left, right
