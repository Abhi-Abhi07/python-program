import sounddevice
from scipy.io.wavfile import write

fs=44100
duration=5
print("recoding start:-")
recod_voice=sounddevice.rec(int(fs*duration), samplerate=fs, channels=2)
sounddevice.wait()
write("C:\PythonProgram\project\output.mp3",fs,recod_voice)
print("voice recoded !")


