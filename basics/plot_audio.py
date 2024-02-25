import wave
import matplotlib.pyplot as plt
import numpy as np
import os

obj = wave.open("./Sports.wav", "rb")
sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)
obj.close()

t_audio = n_samples/sample_freq
print(t_audio)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)
times = np.linspace(0, t_audio, num=n_samples)

plt.figure(figsize=(15,5))
plt.plot(times,signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal wave")
plt.xlabel("Time (s)")
plt.xlim(0,t_audio)
directory_path = '/Users/beyzakaya/Desktop/bk/Proje:Kod/speechRecognition/basics'

if not os.path.exists(directory_path):
    os.makedirs(directory_path)

file_path = os.path.join(directory_path, 'signal_wave.png')
plt.savefig(file_path)

plt.show()



