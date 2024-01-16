## FTT Visualizer
This is written in python. Before running, make sure you have python installed.

## Description & specs
This is a FFT visualizer. FFT is an algorithm to decompose a wave signal into individual frequencies of sine waves, that equal the signal when added together. This program works by using the numpy library to perform a Fast-Fourier transform on a signal that is taken from the microphone of your machine, using the pyaudio library. This data is then displayed using the matplotlib library, a library for simulating matplot in python. The complex number outputted from the Fast Fourier Transform is then inputted to the ```y-data``` of the lines in the Fast Fourier subplots.
## Necessary Settings:
PLEASE NOTE THAT THIS PROGRAM TAKES INPUT FROM MICROPHONE. I used a usb hub that had an option to plug in a 3.5mm aux cable as an microphone input.
In order to use this program properly, please make sure in your settings that you have chosen the correct microphone input, as there is no way (at least in this program) to configure the microphone of your choice. The default mic chosen in this program is the mic chosen and configured in settings. Please take the time to do so before you run the program. In order to get data for analysis, it is best if you keep the input volume of the computer at 100%, and change the playback device's volume as necessary. It is recommended to keep both settings constant for the whole project.
## Dependencies:
Before running, it is neccecary to have the following libraries:

- time
- numpy
- pyaudio
- struct
- matplotlib
- os
## [PIP](https://pip.pypa.io/en/stable/) to install libraries:
Run the following code one by one in your command prompt window, either from an dedicated editor such as [PyCharm](https://www.jetbrains.com/pycharm/download/?section=windows), or the standard cmd.exe or terminal.

```bash
pip install matplotlib
pip install numpy
pip install pyaudio
pip install struct
```
OS and Time libraries are almost always pre-installed with python.

## The code
The code is written below, but can be downloaded from "main.py"

--
Start the code with the following commands to import libraries into your code.
```python
import time as t
import numpy as np #importing Numpy with an alias np
import pyaudio as pa
import struct
import matplotlib.pyplot as plt
import os
import matplotlib.ticker as ticker
```
## Reset and initialize variables and libraries:
Next we have,
```python

folder = input("Folder DIR>>> ")
os.mkdir(folder)
os.chdir(folder)

CHUNK = 1024 * 1
FORMAT = pa.paInt16
CHANNELS = 1
RATE = 44100 # in Hz

avrglst = []

p = pa.PyAudio()

stream = p.open(
   format = FORMAT,
   channels = CHANNELS,
   rate = RATE,
   input=True,
   output=True,
   frames_per_buffer=CHUNK
)
```
## Configure the subplots
Paste this code after:
```python

photo = t.time() + int(input("Photo Delay>> "))
fig, (ax,ax1) = plt.subplots(2)
x_fft = np.linspace(0, RATE, CHUNK)
x = np.arange(0,2*CHUNK,2)
line, = ax.plot(x, np.random.rand(CHUNK),'r')
line_fft, = ax1.semilogx(x_fft, np.random.rand(CHUNK), 'b')
avrgamp, = ax1.semilogx(x_fft, np.random.rand(CHUNK), 'y')
ax.set_ylim(-32000,32000)
ax.ser_xlim = (0,CHUNK)
ax1.set_xlim(int(input("xmin>> ")),int(input("xmax>> ")))
ax1.set_ylim(0,1)
ax1.yaxis.set_major_formatter(ticker.StrMethodFormatter("{x:.2f}"))  # Set the format of the y-axis labels
ax1.set_yticks(np.linspace(ax1.get_yticks()[0], ax1.get_yticks()[-1], 20))
bob = True
freq  = [220, 246, 277, 293, 329, 369, 440, 493, 554, 587, 659, 739, 880, 987, 1108, 1174, 1312, 1479, 1760]
ax1.axvline(x=freq[0], color='g', linestyle='solid')
ax1.axvline(x=freq[1], color='g', linestyle='solid')
ax1.axvline(x=freq[2], color='g', linestyle='solid')
ax1.axvline(x=freq[3], color='g', linestyle='solid')
ax1.axvline(x=freq[4], color='g', linestyle='solid')
ax1.axvline(x=freq[5], color='g', linestyle='solid')
ax1.axvline(x=freq[6], color='g', linestyle='solid')
ax1.axvline(x=freq[7], color='g', linestyle='solid')
ax1.axvline(x=freq[8], color='g', linestyle='solid')
ax1.axvline(x=freq[9], color='g', linestyle='solid')
ax1.axvline(x=freq[10], color='g', linestyle='solid')
ax1.axvline(x=freq[11], color='g', linestyle='solid')
ax1.axvline(x=freq[12], color='g', linestyle='solid')
ax1.axvline(x=freq[13], color='g', linestyle='solid')
ax1.axvline(x=freq[14], color='g', linestyle='solid')
ax1.axvline(x=freq[15], color='g', linestyle='solid')
ax1.axvline(x=freq[16], color='g', linestyle='solid')
ax1.axvline(x=freq[17], color='g', linestyle='solid')
ax1.axvline(x=freq[18], color='g', linestyle='solid')

while bob:
   if input("ADDLINE?>> ") == '1':
       ax1.axvline(x=int(input("x-coordinate>> ")), color='g', linestyle='solid')
   elif input("conf?>> ") == '1':
       bob = False

fig.show()
photoit = 1
```
## The main part:
Finally paste this code:
```python
while 1:
   data = stream.read(CHUNK)
   dataInt = struct.unpack(str(CHUNK) + 'h', data)
   line.set_ydata(dataInt)
   line_fft.set_ydata(np.abs(np.fft.fft(dataInt))*2/(11000*CHUNK))
   avrglst.append(np.abs(np.fft.fft(dataInt))*2/(11000*CHUNK))
   avrgamp.set_ydata(np.mean(avrglst, axis=0))
   fig.canvas.draw()
   if t.time() >= photo:
       fig.savefig(os.path.join(os.getcwd(), "fig"+str(photoit)+".png"))
       photo = t.time() + 5
       photoit = photoit + 1  # Increment photoit for the next iteration
   fig.canvas.flush_events()
```

## How to use
Here is the order it should ask you questions in:
```bash
Folder Dir>>
```
Type in the name of the folder you want the auto photos to be saved in. It will create a folder in the same location as the python program.
```bash
Photo delay>> 
```
Type in the delay (in seconds) between the photos being taken
```bash
xmin>>
```
Type in the minimum X value (atleast 1 or any whole number above)
```bash
xmax>>
```
Type in the maximum x value. (I use 15000)
```bash
Addline?>>
```
Type in 1 for yes, and 0 for no
```bash
x-coordinate?>>
```
Type in the frequecy in hertz of any additional frequencies you want to monitor.
```bash
conf?>>
```
Confirmation. 1 for yes and 0 for no.

## You are all set. This is how to read.
Move cursor over subplots and at the bottom right corner will be the x and y value of the point. The yellow line is the average value of the FTT. Blue line is the current FTT line. Red is the waveform. Green lines are the monitored frequencies, or markers for all the frequencies I monitored in my experiment.

## Thank You for Using My Program!

