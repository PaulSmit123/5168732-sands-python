import numpy as np

from signals import generate_sine_wave, generate_step_function
from operations import time_shift, time_scale


def test_generate_sine_wave_length():
    fs = 200
    duration = 2.0
    f = 5.0
    x = generate_sine_wave(f, duration, fs)

    assert len(x) == int(fs * duration)


def test_generate_step_function_levels():
    fs = 10
    duration = 2.0
    step_time = 0.5
    x = generate_step_function(step_time, duration, fs)

    n_step = int(step_time * fs)
    assert np.allclose(x[:n_step], 0.0)
    assert np.allclose(x[n_step:], 1.0)


def test_time_shift_zero():
    x = np.array([1.0, 2.0, 3.0])
    y = time_shift(x, sample_rate=10, shift_seconds=0.0)

    assert np.allclose(y, x)
