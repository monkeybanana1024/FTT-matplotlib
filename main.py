import time as t
import numpy as np #importing Numpy with an alias np
import pyaudio as pa
import struct
import matplotlib.pyplot as plt
import os
import matplotlib.ticker as ticker

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
photoit = 1  # Initialize photoit outside the while loop
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


