import numpy as np
import matplotlib.pyplot as plt

from signals import generate_sine_wave, generate_step_function
from operations import time_shift, time_scale

# --------------------
# Parameters
# --------------------
fs = 200            # samples per second
duration = 2.0      # seconds
f = 5.0             # sine frequency in Hz
step_time = 0.5     # second at which the step jumps to 1
shift_seconds = 0.3 # positive = delay (shift right)
scale_factor = 0.5  # 0.5 (longer) or 1.5 (shorter) depending on time_scale()

# --------------------
# Generate signals
# --------------------
sine = generate_sine_wave(f, duration, fs)
step = generate_step_function(step_time, duration, fs)

# Time axes (match lengths)
t_sine = np.arange(len(sine)) / fs
t_step = np.arange(len(step)) / fs

# --------------------
# Apply operations
# --------------------
sine_shifted = time_shift(sine, fs, shift_seconds)
sine_scaled  = time_scale(sine, scale_factor)

step_shifted = time_shift(step, fs, shift_seconds)
step_scaled  = time_scale(step, scale_factor)

# Time axes for scaled signals (length changes)
t_sine_scaled = np.arange(len(sine_scaled)) / fs
t_step_scaled = np.arange(len(step_scaled)) / fs

# --------------------
# Plot
# --------------------
plt.figure(figsize=(11, 8))

# Row 1: SINE
plt.subplot(2, 3, 1)
plt.plot(t_sine, sine)
plt.title("Sine — original")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.subplot(2, 3, 2)
plt.plot(t_sine, sine_shifted)
plt.title(f"Sine — shifted by {shift_seconds}s")
plt.xlabel("Time [s]")

plt.subplot(2, 3, 3)
plt.plot(t_sine_scaled, sine_scaled)
plt.title(f"Sine — scaled (factor={scale_factor})")
plt.xlabel("Time [s]")

# Row 2: STEP
plt.subplot(2, 3, 4)
plt.plot(t_step, step)
plt.title("Step — original")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")

plt.subplot(2, 3, 5)
plt.plot(t_step, step_shifted)
plt.title(f"Step — shifted by {shift_seconds}s")
plt.xlabel("Time [s]")

plt.subplot(2, 3, 6)
plt.plot(t_step_scaled, step_scaled)
plt.title(f"Step — scaled (factor={scale_factor})")
plt.xlabel("Time [s]")

plt.tight_layout()
plt.savefig("demo_signals.png")  
plt.show()
