import numpy as np

def time_shift(x, sample_rate, shift_seconds):
    """
    Shift a signal in time.

    Parameters:
        x (numpy.ndarray): Input signal
        sample_rate (int): Number of samples per second
        shift_seconds (float): Amount of time (seconds) to shift

    Returns:
        numpy.ndarray: Time-shifted signal
    """
    n = len(x)
    k = int(round(shift_seconds * sample_rate))
    if k == 0:
        return x.copy()
    if k > 0:
        return np.concatenate([np.zeros(k), x])[:n]
    k = -k
    return np.concatenate([x[k:], np.zeros(k)])[:n]


def time_scale(x, scale):
    """
    Stretch or compress a signal in time.

    Parameters:
        x (numpy.ndarray): Input signal
        scale (float): Scaling factor (>1 = stretch, <1 = compress)

    Returns:
        numpy.ndarray: Time-scaled signal
    """
    n = len(x)
    if n == 0:
        return x.copy()
    new_len = int(np.floor((n - 1) / scale)) + 1
    t_old = np.arange(n)
    t_new = np.arange(new_len)
    return np.interp(scale * t_new, t_old, x)
