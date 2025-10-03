import numpy as np

def create_unit_step(step_time, duration):
    t = np.linspace(0, duration, int(44100 * duration))
    return np.where(t >= step_time, 1.0, 0.0)

print(create_unit_step(1.0, 2))

def create_sine_wave(frequency, duration):
    t = np.linspace(0, duration, int(44100 * duration))
    return np.sin(2 * np.pi * frequency * t)

print(create_sine_wave(440, 2))