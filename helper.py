import numpy as np

def create_unit_step(step_time, duration):
    t = np.linspace(0, duration, int(44100 * duration))
    return np.where(t >= step_time, 1.0, 0.0)

def create_sine_wave(frequency, duration):
    t = np.linspace(0, duration, int(44100 * duration))
    return np.sin(2 * np.pi * frequency * t)

def test_create_unit_step():
    result = create_unit_step(1.0, 2.0)
    assert len(result) == 88200
    assert result[0] == 0
    assert result[-1] == 1

def test_create_sine_wave():
    result = create_sine_wave(440, 1.0)
    assert len(result) == 44100  
    assert result[0] == 0  
    
    assert np.isclose(max(result), 1, atol=1e-2)