import matplotlib.pyplot as plt
from scipy.io import wavfile


sample_rate, data = wavfile.read('../clues/audio/sigil1.wav')
plt.specgram(data, Fs=sample_rate)
plt.axis('off')
plt.savefig('../clues/audio/sigil1_spectrogram.png')
