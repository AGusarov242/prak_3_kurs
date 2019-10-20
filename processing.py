import warnings
warnings.filterwarnings('ignore')
import librosa
import os
import numpy as np
import soundfile
import audioread

from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed

def extract_mfcc(sub_folder, output_folder):
    output_path = "{}/{}".format(output_folder, sub_folder[0])
    os.makedirs(output_path, exist_ok=True)
    for i in sub_folder[2]:
        audio_time_series, sampling_rate = librosa.core.load("{}/{}".format(sub_folder[0],i))
        mfcc_features = np.empty(0)
        mfcc_features = librosa.feature.mfcc(audio_time_series, sampling_rate)
        np.save("{}/{}".format(output_path, i), mfcc_features)