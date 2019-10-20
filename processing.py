import warnings
warnings.filterwarnings('ignore')
import librosa
import os
import numpy as np
import soundfile
import audioread

from multiprocessing import Process
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed

def extract_mfcc(sub_folder, output_folder, path):
    output_path = "{}/{}".format(output_folder, path)
    os.makedirs(output_path, exist_ok=True)
    for i in sub_folder[2]:
        audio_time_series, sampling_rate = librosa.core.load("{}/{}".format(sub_folder[0],i))
        mfcc_features = np.empty(0)
        mfcc_features = librosa.feature.mfcc(audio_time_series, sampling_rate)
        np.save("{}/{}".format(output_path, i), mfcc_features)
        
def processes(input_folder, output_folder, processes_count):
    main_folder = os.walk(input_folder)
    with ProcessPoolExecutor(max_workers=processes_count) as pool:
        for sub_folder in main_folder:
            path = sub_folder[0]
            if sub_folder[2]:
                pool.submit(extract_mfcc, sub_folder, output_folder, path)
                
processes("aac1", "new_aac", 7) 
