import numpy as np
from scipy.stats import ks_2samp


chat_id = 461694118



def solution(x: np.array, y: np.array) -> bool:
    ks_statistic, p_value = ks_2samp(x, y)

    alpha = 0.03

    if p_value < alpha:
        return True
    else:
        return False
