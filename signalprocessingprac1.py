import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt 

Y,sr=librosa.load("exhibition_sn10.wav",sr=None)

Y=np.fft.fft(Y)
frequency=np.fft.fftfreq(len(Y),d=1/sr )
half=len(Y)//2
Y=np.abs(Y[:half])
frequency=frequency[:half]
plt.figure()
plt.plot(frequency,Y)
plt.xlabel ("Frequency")
plt.ylabel(" Amplitude ")
plt.title("FFT")
plt.show()
