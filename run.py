from signals import generate_sine_wave
import matplotlib.pyplot as plt   

# Parameters
frequency = 5        # Hz
duration = 2         # seconds
sample_rate = 100    # samples per second

# Generate the sine wave
wave = generate_sine_wave(frequency, duration, sample_rate)

# Print first 10 samples
print(wave[:10])


t = [i / sample_rate for i in range(len(wave))]


plt.plot(t, wave)
plt.title("Sine Wave")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.show()
