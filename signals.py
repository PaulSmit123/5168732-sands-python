import numpy as np

def generate_sine_wave(frequency, duration, sample_rate):
    """
    Generate a sine wave signal.

    Parameters:
        frequency (float): Frequency of the sine wave in Hz.
        duration (float): Duration of the signal in seconds.
        sample_rate (int): Number of samples per second.

    Returns:
        numpy.ndarray: Array containing the sine wave values.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.sin(2 * np.pi * frequency * t)
    return signal


def generate_step_function(step_time, duration, sample_rate):
    """
    Generate a step function signal.

    Parameters:
        step_time (float): The time (in seconds) when the step occurs.
        duration (float): Duration of the signal in seconds.
        sample_rate (int): Number of samples per second.

    Returns:
        numpy.ndarray: Array containing the step function values.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = np.zeros_like(t)
    signal[t >= step_time] = 1.0
    return signal

