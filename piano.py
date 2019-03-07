import math
import pyaudio
from time import sleep

PyAudio = pyaudio.PyAudio


def tocar(nota,tempo):
	BITRATE = 30000 #160000
	LENGTH = tempo
	nota = nota.lower()

	if nota == "c5":
		FREQUENCY = 523.3
	elif nota == "d5":
		FREQUENCY = 587.3
	elif nota == "e5":
		FREQUENCY = 659.3
	elif nota == "f5":
		FREQUENCY = 698.5
	elif nota == "g5":
		FREQUENCY = 784.0
	elif nota == "a5":
		FREQUENCY = 880.0
	elif nota == "b5":
		FREQUENCY = 987.8
	elif nota == "c4":
		FREQUENCY = 261.6
	elif nota == "d4":
		FREQUENCY = 293.7
	elif nota == "e4":
		FREQUENCY = 329.6
	elif nota == "f4":
		FREQUENCY = 349.2
	elif nota == "g4":
		FREQUENCY = 392.0
	elif nota == "a4":
		FREQUENCY = 440.0
	elif nota == "b4":
		FREQUENCY = 493.9
	elif nota == "b4b":
		FREQUENCY = 466.2
	else:
		FREQUENCY = 261.6

	if FREQUENCY > BITRATE:
		BITRATE = FREQUENCY+100

	NUMBEROFFRAMES = int(BITRATE * LENGTH)
	RESTFRAMES = NUMBEROFFRAMES % BITRATE
	WAVEDATA = ''    

	for x in range(NUMBEROFFRAMES):
		WAVEDATA += chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))    

	for x in range(RESTFRAMES):
		WAVEDATA += chr(128)

	p = PyAudio()
	stream = p.open(format = p.get_format_from_width(1),
		channels = 1,
		rate = BITRATE,
		output = True)

	stream.write(WAVEDATA)
	stream.stop_stream()
	stream.close()
	p.terminate()

tocar("E5",0.1)
tocar("E5",0.07)
tocar("E5",0.07)
tocar("C5",0.1)
tocar("E5",0.1)
tocar("G5",0.2)
tocar("G4",0.2)
tocar("C5",0.1)
tocar("G4",0.1)
tocar("E4",0.2)
tocar("A4",0.1)
tocar("B4",0.1)
tocar("B4b",0.1)
tocar("A4",0.1)
tocar("G4",0.1)