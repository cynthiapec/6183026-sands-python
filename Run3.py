from helper import create_unit_step, create_sine_wave
import numpy as np
import matplotlib.pyplot as plt

unit_step_signal = create_unit_step(1.5, 2)
sine_signal = create_sine_wave(5, 2)

modified_unit_step = unit_step_signal * 2  
modified_sine = sine_signal * 0.5  

t1 = np.linspace(0, 2, len(unit_step_signal))
t2 = np.linspace(0, 2, len(sine_signal))

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(t1, modified_unit_step)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Modified Unit Step Signal (2x amplitude and shifted by 0.5s)")

plt.subplot(1, 2, 2)
plt.plot(t2, modified_sine)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Modified Sine Wave (0.5x amplitude)')

plt.tight_layout()
plt.show()