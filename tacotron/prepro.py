# -*- coding: utf-8 -*-
#/usr/bin/python2
'''
By kyubyong park and tommy mulc. kbpark.linguist@gmail.com. tmulc18@gmail.com.
https://www.github.com/kyubyong/tacotron
'''

from __future__ import print_function

from multiprocessing import Process, Pool
from utils import load_spectrograms
import os
from data_load import load_data
import numpy as np
import tqdm
from hyperparams import Hyperparams as hp
from tqdm import *

NUM_JOBS = 4

# Utility function
def f(fpath):
    fname, mel, mag = load_spectrograms(fpath)
    np.save("{}/mels/{}".format(hp.lang, fname.replace("wav", "npy")), mel)
    np.save("{}/mags/{}".format(hp.lang, fname.replace("wav", "npy")), mag)
    return None

# Load data
fpaths, _, _ = load_data() # list

# Creates folders
if not os.path.exists("{}/mels".format(hp.lang)): os.makedirs("{}/mels".format(hp.lang))
if not os.path.exists("{}/mags".format(hp.lang)): os.makedirs("{}/mags".format(hp.lang))

# Creates pool
p = Pool(NUM_JOBS)

total_files = len(fpaths)
with tqdm(total=total_files) as pbar:
	for i, _ in tqdm(enumerate(p.imap_unordered(f, fpaths))):
		pbar.update()