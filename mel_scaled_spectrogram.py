import os
import time
import matplotlib 
import pylab 
import librosa 
import librosa.display 
import numpy as np 

def extractSpectrogram(y, sr):
  curr_time = int(round(time.time()*1000))
  save_path = 'tmp/{}.jpg'.format(curr_time) 
  pylab.axis('off')
  pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])
  S = librosa.feature.melspectrogram(y=y, sr=sr) 
  librosa.display.specshow(librosa.power_to_db(S, ref=np.max)) 
  pylab.savefig(save_path, bbox_inches=None, pad_inches=0) 
  pylab.close()

# y  => audio time series
# sr => sampling rate of y
if __name__ == "__main__":
  y, sr = librosa.load('sample/output.wav')
  extractSpectrogram(y, sr)

